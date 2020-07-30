import configparser
import boto3
import json

def create_clients(config):
    print('## Remove Client Redshift and IAM')
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
    print('## Remove Redshift Cluster {}'.format(config['DWH']['DWH_CLUSTER_IDENTIFIER']))
    redshift.delete_cluster( ClusterIdentifier=config['DWH']['DWH_CLUSTER_IDENTIFIER'],  SkipFinalClusterSnapshot=True)

def remove_resource(config, iam):
    print('## Remove Resource Cluster {}'.format(config['DWH']['DWH_CLUSTER_IDENTIFIER']))
    iam.detach_role_policy(RoleName=config['DWH']['DWH_IAM_ROLE_NAME'], PolicyArn="arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess")
    iam.delete_role(RoleName=config['DWH']['DWH_IAM_ROLE_NAME'])

def empty_bucket(config):
    print('## Clean bucket {}'.format(config["S3"]["bucket_name"]))
    client = boto3.client('s3',
                      region_name=config['AWS']['REGION'],
                      aws_access_key_id=config['AWS']['KEY'],
                      aws_secret_access_key=config['AWS']['SECRET'])
    
    response = client.list_objects_v2(Bucket=config["S3"]["bucket_name"])
    if 'Contents' in response:
        for item in response['Contents']:
            client.delete_object(Bucket=config["S3"]["bucket_name"], Key=item['Key'])
            while response['KeyCount'] == 1000:
                response = client.list_objects_v2(Bucket=config["S3"]["bucket_name"], StartAfter=response['Contents'][0]['Key'])
        for item in response['Contents']:
            client.delete_object(Bucket=config["S3"]["bucket_name"], Key=item['Key'])

def delete_bucket(config):
    print('## Remove bucket {}'.format(config["S3"]["bucket_name"]))
    client = boto3.client('s3',
                      region_name=config['AWS']['REGION'],
                      aws_access_key_id=config['AWS']['KEY'],
                      aws_secret_access_key=config['AWS']['SECRET'])
    try:
        client.delete_bucket(Bucket=config["S3"]["bucket_name"])
        print("## Bucket {} delete !".format(config["S3"]["bucket_name"]))
    except e:
        print("Error: can't delete bucket")

def update_cfg():
    print('## Remove data config')
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
    empty_bucket(config)
    delete_bucket(config)
    update_cfg()

if __name__ == "__main__":
    main()
