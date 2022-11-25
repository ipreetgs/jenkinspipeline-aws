import boto3
import sys

BucketName = sys.argv[1]
AWS_REGION = "us-east-1"
session = boto3.session.Session()
s3_client = session.client('s3')

# <<<<<<<<<    code for bucket creation  >>>>>>>

client = boto3.client('s3')

response = client.create_bucket(Bucket=BucketName)

print("Amazon S3 bucket has been created")
