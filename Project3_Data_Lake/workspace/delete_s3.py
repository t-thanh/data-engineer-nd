import boto3    
from create_s3 import get_key_secret

def get_s3(region, KEY, SECRET):
    """ Get the current s3, both client and resource
    """
    s3_resource = boto3.resource('s3', 
                                 region_name=region,
                                 aws_access_key_id=KEY,
                                 aws_secret_access_key=SECRET)
    
    s3_client = boto3.client('s3', 
                             region_name=region,
                             aws_access_key_id=KEY,
                             aws_secret_access_key=SECRET)
    
    return s3_resource, s3_client

def delete_all(s3_resource, s3_client, bucket_name):
    """ Empty and delete s3
    """
    bucket = s3_resource.Bucket(bucket_name)
    bucket.objects.all().delete()
    print('###')
    print('Empty s3: ' + bucket_name)
    print('###')
    s3_client.delete_bucket(Bucket = bucket_name)
    print('###')
    print('Delete s3 ' + bucket_name)
    print('###')

if __name__ == '__main__':
    KEY, SECRET = get_key_secret()
    s3_resource, s3_client = get_s3('us-west-2', KEY, SECRET)
    delete_all(s3_resource, s3_client, 'udacity-data-lake-project')