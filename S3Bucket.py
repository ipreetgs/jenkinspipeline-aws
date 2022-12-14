import boto3
import sys

BucketName = sys.argv[1]
ExpDay =int(sys.argv[2])
TransDay = int(sys.argv[3])
oth = int(sys.argv[4]
AWS_REGION = "us-east-1"

#<<<< functions>>>>
def CreateBucket(BucketName):
    session = boto3.session.Session()
    s3_client = session.client('s3')
    client = boto3.client('s3')
    try:
        response = client.create_bucket(Bucket=BucketName)
        print(f'Bucket {BucketName} created')
    except Exception as E:
        print(E)
        print("some Error in creating bucket")

#<<<<<<< code for vers....ing >>>>>>>>

def VerSonEnable(bucket_name):
    resource_for_s3 = boto3.resource("s3", region_name=AWS_REGION)
    versioning = resource_for_s3.BucketVersioning(bucket_name)
    versioning.enable()
    print(f'versioning is enabled for S3 Bucket: {versioning.status}')

# <<<<<<< lifecycle rule >>>>>>>>>

def LifeCycle_Mgmt(BucketName,ExpDay,TransDay,Oth):

    s3=boto3.resource('s3')
    bucket_lifecycle_configuration=s3.BucketLifecycleConfiguration(BucketName)
    response=bucket_lifecycle_configuration.put(
        # ChecksumAlgorithm='CRC32'|'CRC32C'|'SHA1'|'SHA256',
        LifecycleConfiguration={
            'Rules': [
                {
                    'Expiration': {
                        'Days': ExpDay,
                        'ExpiredObjectDeleteMarker': True
                    },
                    'ID': 'demorule',
                    'Filter': {
                    },
                    'Status': 'Enabled',
                    'Transitions': [
                        {
                            # 'Date': datetime(2015, 1, 1),

                            'Days': TransDay,
                            'StorageClass': 'GLACIER'

                            # |'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'|'GLACIER_IR'
                        },
                    ],
                    'NoncurrentVersionTransitions': [
                        {
                            'NoncurrentDays': Oth,
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
        # ExpectedBucketOwner='demo'
    )

# <<<<<< code >>>>
# << check if bucket already exixts:>>
s3 = boto3.resource('s3')
AWS_buckets = [bucket.name for bucket in s3.buckets.all()]
if BucketName in AWS_buckets:
    print("Bucket already avaliable")
    # VerSonEnable(BucketName)
    # LifeCycle_Mgmt(BucketName,ExpDay,TransDay,oth)


else:
    print("name not found: Creating one!!!!!!")
    CreateBucket(BucketName)
    VerSonEnable(BucketName)
    LifeCycle_Mgmt(BucketName,ExpDay,TransDay,oth)


