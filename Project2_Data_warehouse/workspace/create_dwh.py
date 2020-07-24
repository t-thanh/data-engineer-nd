import configparser
import boto3
import json
import time
import pandas as pd

def create_clients(config):
    print('=== Creating a Clients')
    print('From AWS region {}'.format(config['AWS']['REGION']))
    
    iam = boto3.client('iam',
                       region_name=config['AWS']['REGION'],
                       aws_access_key_id=config['AWS']['KEY'], 
                       aws_secret_access_key=config['AWS']['SECRET'])

    redshift = boto3.client('redshift',
                           region_name=config['AWS']['REGION'],
                           aws_access_key_id=config['AWS']['KEY'],
                           aws_secret_access_key=config['AWS']['SECRET'])

    return iam, redshift;

def create_iam_role(config, iam):
    from botocore.exceptions import ClientError
    try:
        print('=== Creating a new IAM Role')
        dwhRole = iam.create_role(
            Path='/',
            RoleName=config['DWH']['DWH_IAM_ROLE_NAME'],
            Description = "Allows Redshift clusters to call AWS services on your behalf.",
            AssumeRolePolicyDocument=json.dumps(
                {'Statement': [{'Action': 'sts:AssumeRole',
                   'Effect': 'Allow',
                   'Principal': {'Service': 'redshift.amazonaws.com'}}],
                   'Version': '2012-10-17'})
        )
    except Exception as e:
        print(e)

def attach_policy(config, iam):
    print('=== Attaching Policy')
    iam.attach_role_policy(RoleName=config['DWH']['DWH_IAM_ROLE_NAME'],
                           PolicyArn="arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
                          )['ResponseMetadata']['HTTPStatusCode']

def get_role_arn(config, iam):
    print('=== Getting the IAM role ARN')
    roleArn = iam.get_role(RoleName=config['DWH']['DWH_IAM_ROLE_NAME'])['Role']['Arn']
    return roleArn
    
def create_redshift_cluster(config, redshift, roleArn):
    print('=== Creating Redshit Cluster')
    from botocore.exceptions import ClientError
    try:
        response = redshift.create_cluster(        
            # Parameters for hardware DWH
            ClusterType=config['DWH']['DWH_CLUSTER_TYPE'],
            NodeType=config['DWH']['DWH_NODE_TYPE'],
            NumberOfNodes=int(config['DWH']['DWH_NUM_NODES']),        

            # Parameters for identifiers & credentials
            DBName=config['DWH']['DWH_DB'],
            ClusterIdentifier=config['DWH']['DWH_CLUSTER_IDENTIFIER'],
            MasterUsername=config['DWH']['DWH_DB_USER'],
            MasterUserPassword=config['DWH']['DWH_DB_PASSWORD'],        

            # Parameter for role (to allow s3 access)
            IamRoles=[roleArn]         
        )
    except Exception as e:
        print(e)
        
    print('Wait, Checking the status of {} redshift cluster'.format(config['DWH']['DWH_CLUSTER_IDENTIFIER']))
    is_create_redshift = False
    
    while not is_create_redshift:
        time.sleep(15)
        myClusterProps = redshift.describe_clusters(ClusterIdentifier=config['DWH']['DWH_CLUSTER_IDENTIFIER'])['Clusters'][0]
        print('Cluster`s status is: {}'.format(myClusterProps['ClusterStatus']))
        is_create_redshift = myClusterProps['ClusterStatus'] == 'available'

    print('Redshift cluster {} created.'.format(config['DWH']['DWH_CLUSTER_IDENTIFIER']))
    
    ''' Open TCP port to access cluster's endpoint
    try:
        vpc = ec2.Vpc(id=myClusterProps['VpcId'])
        for sg in (vpc.security_groups.all()):
            if (sg.group_name) == "default":
                defaultSg=sg
                break    

        defaultSg.authorize_ingress(
            GroupName= defaultSg.group_name,
            CidrIp='0.0.0.0/0',
            IpProtocol='TCP',
            FromPort=int(config['DWH']['DWH_PORT']),
            ToPort=int(config['DWH']['DWH_PORT'])
        )
    except boto_exceptions.ClientError as e:
        print(e)
        print("Service Group Ingress already setup")
    except Exception as e:
        print(e)
        raise 
        '''
        
    return myClusterProps

def pretty_redshift_props(props):
    pd.set_option('display.max_colwidth', -1)
    keysToShow = ["ClusterIdentifier", "NodeType", "ClusterStatus", "MasterUsername", "DBName", "Endpoint", "NumberOfNodes", 'VpcId']
    x = [(k, v) for k,v in props.items() if k in keysToShow]
    return pd.DataFrame(data=x, columns=["Key", "Value"])

def update_cfg(endpoint, arn):
    cfg = configparser.ConfigParser()
    cfg.read('dwh.cfg')
    cfg.set('CLUSTER', 'HOST', endpoint)
    cfg.set('IAM_ROLE', 'ARN', arn)
    with open('dwh.cfg', "w") as config_file:
        cfg.write(config_file)
        
def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    client_iam, client_redshift = create_clients(config)
    create_iam_role(config, client_iam)
    attach_policy(config, client_iam)
    role_arn = get_role_arn(config, client_iam)
    
    clusterProps = create_redshift_cluster(config, client_redshift, role_arn)
    if (clusterProps):
        print(pretty_redshift_props(clusterProps))
        update_cfg(clusterProps['Endpoint']['Address'], clusterProps['IamRoles'][0]['IamRoleArn'])
        print('DWH_ENDPOINT :: {}'.format(clusterProps['Endpoint']['Address']))
        print('DWH_ROLE_ARN :: {}'.format(clusterProps['IamRoles'][0]['IamRoleArn'])) 
        

if __name__ == "__main__":
    main()