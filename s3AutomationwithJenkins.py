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
VerSonEnable(BucketName)

#<<<lifecycle>>
s3=boto3.resource('s3')
bucket_lifecycle_configuration=s3.BucketLifecycleConfiguration(BucketName)
response=bucket_lifecycle_configuration.put(
    # ChecksumAlgorithm='CRC32'|'CRC32C'|'SHA1'|'SHA256',
    LifecycleConfiguration={
        'Rules': [
            {
                'Expiration': {
                    'Days': 15,
                    'ExpiredObjectDeleteMarker': True
                },
                'ID': 'demorule',
                'Filter': {
                },
                'Status': 'Enabled',
                'Transitions': [
                    {
                        # 'Date': datetime(2015, 1, 1),

                        'Days': 23,
                        'StorageClass': 'GLACIER'

                        # |'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'|'GLACIER_IR'
                    },
                ],
                'NoncurrentVersionTransitions': [
                    {
                        'NoncurrentDays': 23,
                        'StorageClass': 'STANDARD_IA',
                        'NewerNoncurrentVersions': 23
                    },
                ],
                'NoncurrentVersionExpiration': {
                    'NoncurrentDays': 123,
                    'NewerNoncurrentVersions': 123
                },
                'AbortIncompleteMultipartUpload': {
                    'DaysAfterInitiation': 123
                }
            },
        ]
    },
    ExpectedBucketOwner='demo'
)




print("Amazon S3 bucket has been created")
