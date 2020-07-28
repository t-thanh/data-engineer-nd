import logging
import boto3
from botocore.exceptions import ClientError
from glob import glob as globlin
import configparser


def get_key_secret():
    
    """ Getting key and secret from the config file
    """
    
    config = configparser.ConfigParser()
    config.read('dl.cfg')

    KEY = config['AWS']['AWS_ACCESS_KEY_ID']
    SECRET = config['AWS']['AWS_SECRET_ACCESS_KEY']
    return KEY, SECRET


def get_data_files(path):
    """ Get the paths of all filenames to be uploaded        
    """
    print('###')
    print('Log data list')
    print('###')
    log_files_list = globlin(path + '/*/*.json' , recursive=True)
    song_files_list = globlin(path + '/*/*/*/*/*.json', recursive=True)
    print(log_files_list)
    print('###')
    print('Song data list')
    print('###')
    print(song_files_list)
    return log_files_list, song_files_list


def create_bucket(bucket_name, KEY, SECRET, region=None):
    """ Create S3 bucket in us-west-2
    """
    ## Creating the bucket 
    try:
        if region is None:
            s3_client = boto3.client('s3', 
                                     aws_access_key_id=KEY,
                                     aws_secret_access_key=SECRET)
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', 
                                     region_name=region,
                                     aws_access_key_id=KEY,
                                     aws_secret_access_key=SECRET)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        print('Could not create')
        exit()
        
    print('###')
    print('Create S3 Client')
    print('###')
    return s3_client
       
        
        
def upload_file_s3(file_name, bucket):
    """ Upload a file to an S3 bucket
    """
    try:
        response = s3_client.upload_file(file_name.replace('./',''), 
                                         bucket, 
                                         file_name.replace('./',''))
        print("Uploaded " + file_name)
    except ClientError as e:
        print("Failed to upload " + file_name)
        logging.error(e)
        return False
    return True



def upload_files_s3(files, bucket):
    """ Upload multiple files to s3
    """
        
    print('###')
    print('Uploading files to s3...')
    print('###')
    for i in range(len(files)):
        upload_file_s3(files[i], bucket)
    
    print('###')
    print('Upload complete')
    print('###')
    
if __name__ == '__main__':
    
    KEY, SECRET = get_key_secret()
    
    s3_client = create_bucket('udacity-data-lake-project',
                              KEY,
                              SECRET,
                              'us-west-2')
    log_files_list, song_files_list = get_data_files('./ExtractedData')
    
    upload_files_s3(log_files_list, 
                    'udacity-data-lake-project')
    
    upload_files_s3(song_files_list, 
                    'udacity-data-lake-project')