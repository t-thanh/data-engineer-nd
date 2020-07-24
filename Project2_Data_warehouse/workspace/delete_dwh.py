import configparser
import boto3
import json
import time

def create_clients(config):
    '''Creating a Client Redshift and IAM
    '''
    print('=== Creating a Client Redshift and IAM')
    redshift = boto3.client('redshift',
                           region_name=config['AWS']['REGION'],
                           aws_access_key_id=config['AWS']['KEY'],
                           aws_secret_access_key=config['AWS']['SECRET'])
    iam = boto3.client('iam',
                       region_name=config['AWS']['REGION'],
                       aws_access_key_id=config['AWS']['KEY'], 
                       aws_secret_access_key=config['AWS']['SECRET'])

    return redshift, iam;

def remove_redshift(config, redshift):
    '''Remove Redshift Cluster
    '''
    print('=== Removing Redshift Cluster {}'.format(config['DWH']['DWH_CLUSTER_IDENTIFIER']))
    redshift.delete_cluster( ClusterIdentifier=config['DWH']['DWH_CLUSTER_IDENTIFIER'], 
                                SkipFinalClusterSnapshot=True)
    is_delete_redshift = False
    
    while not is_delete_redshift:
        try:
            myClusterProps = redshift.describe_clusters(ClusterIdentifier=config['DWH']['DWH_CLUSTER_IDENTIFIER'])['Clusters'][0]
            print('Cluster`s status is: {}'.format(myClusterProps['ClusterStatus']))
            time.sleep(15)
            is_delete_redshift = myClusterProps is None
        except redshift.exceptions.ClusterNotFoundFault:
            break

def remove_resource(config, iam):
    '''Remove Resource Cluster
    '''
    print('=== Removing Resource Cluster {}'.format(config['DWH']['DWH_CLUSTER_IDENTIFIER']))
    iam.detach_role_policy(RoleName=config['DWH']['DWH_IAM_ROLE_NAME'], PolicyArn="arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess")
    iam.delete_role(RoleName=config['DWH']['DWH_IAM_ROLE_NAME'])

def update_cfg():
    '''Update config file
    '''
    print('=== Remove data config')
    cfg = configparser.ConfigParser()
    cfg.read('dwh.cfg')
    cfg.set('CLUSTER', 'HOST', '')
    cfg.set('IAM_ROLE', 'ARN', '')
    cfg.set('AWS', 'KEY', '')
    cfg.set('AWS', 'SECRET', '')
    cfg.set('AWS', 'REGION', '')
    with open('dwh.cfg', "w") as config_file:
        cfg.write(config_file)
        
def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    c_redshift, c_iam = create_clients(config)
    remove_redshift(config, c_redshift)
    remove_resource(config, c_iam)
    update_cfg()

if __name__ == "__main__":
    main()