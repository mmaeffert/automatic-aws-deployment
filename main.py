import sys
import boto3
import os
from python_terraform import Terraform
import configparser





# Parses the credentials from the aws-credentials.tfvars file
def parse_credentials():
    with open('./terraform/aws-credentials.tfvars', 'r') as f:
        config_string = '[dummy_section]\n' + f.read()
    # Create a configparser object
    config = configparser.ConfigParser()
    
    # Specify the path to your configuration file
    config_file_path = './aws-credentials.tfvars'

    # Read the configuration file
    config.read_string(config_string)
    access_key = config['dummy_section']['access_key'].replace("\"", "")
    access_secret = config['dummy_section']['secret_key'].replace("\"", "")

    return access_key, access_secret





# Creates the AWS Bucket according to config
def create_bucket():
    tf = Terraform(working_dir='./terraform/')
    apply_output = tf.apply(
        var={"bucket_name": bucket_name}, 
        var_file="aws-credentials.tfvars",
        skip_plan=True
    )



def upload_object():
    with open(os.getcwd() + "/" + file_name, "rb") as file:
        file_content = file.read()

    access_key, access_secret = parse_credentials()

    s3 = boto3.client(
        "s3",
        aws_access_key_id=access_key,
        aws_secret_access_key=access_secret,
        region_name="eu-central-1"
    )

    # Put file
    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=file_content
    )
    



if len(sys.argv) < 3:
    print("Usage: python script.py <bucket name> <file name>")
    sys.exit(1)

bucket_name = sys.argv[1]
file_name = sys.argv[2]

create_bucket()
upload_object()


