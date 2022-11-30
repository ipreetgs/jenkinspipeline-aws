import boto3
import sys
from botocore import ClientError

BucketName = sys.argv[1]
AWS_REGION = "us-east-1"

session = boto3.session.Session()
s3_client = session.client('s3')

# <<<<<<<<<    code for bucket creation  >>>>>>>

client = boto3.client('s3')

response = client.create_bucket(Bucket=BucketName)

#<<<<<<<<vers>>>>>>
resource_for_s3 = boto3.resource("s3", region_name=AWS_REGION)

def VerSonEnable(bucket_name):
    versioning = resource_for_s3.BucketVersioning(bucket_name)
    versioning.enable()

    print(f'Wow, Your versioning is enabled for S3 Bucket: {versioning.status}')


#<<<lifecycle>>
s3=boto3.resource('s3')
Bucket_Lifecycle=s3.BucketLifecycle(BucketName)


VerSonEnable(BucketName)

print("Amazon S3 bucket has been created")
