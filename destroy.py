import sys
import boto3
import os
from python_terraform import Terraform
import configparser






# Creates the AWS Bucket according to config
def create_bucket():
    tf = Terraform(working_dir='./terraform/')
    apply_output = tf.apply(
        var={"bucket_name": bucket_name}, 
        var_file="aws-credentials.tfvars",
        skip_plan=True,
        destroy=True,
    )
    print(apply_output)


if len(sys.argv) < 2:
    print("Usage: python script.py <bucket name>")
    sys.exit(1)

bucket_name = sys.argv[1]

create_bucket()


