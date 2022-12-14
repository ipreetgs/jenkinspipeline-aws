import boto3
import sys

BucketName = sys.argv[1]
TransDays =int(sys.argv[2])
NonCrV = int(sys.argv[3])
ExpDays = int(sys.argv[4])
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
def LifeCycle_Mgmt(BucketName,TransDays,NonCrV,ExpDays)
    client=boto3.client('s3')
    response = client.put_bucket_lifecycle_configuration(
        Bucket=BucketName,
        LifecycleConfiguration={
            'Rules': [
                {
                    'Expiration': {
                        'Days': 91,
                    },
                    'ID': 'move to glacier',
                    'Prefix': '',
                    'Status': 'Enabled',
                    'Transitions': [
                        {
                            'Days': TransDays,
                            'StorageClass': 'STANDARD_IA'
                        },
                    ],
                    'NoncurrentVersionTransitions': [
                        {
                            'NoncurrentDays': NonCrV,
                            'StorageClass': 'GLACIER'
                        },
                    ],
                    'NoncurrentVersionExpiration': {
                        'NoncurrentDays': ExpDays
                    }
                },
            ]
        }
    )
# <<<<<< code >>>>
# << check if bucket already exixts:>>
s3 = boto3.resource('s3')
AWS_buckets = [bucket.name for bucket in s3.buckets.all()]
if BucketName in AWS_buckets:
    print("Bucket already avaliable")
    VerSonEnable(BucketName)
    LifeCycle_Mgmt(BucketName,ExpDay,TransDay,oth)


else:
    print("name not found: Creating one!!!!!!")
    CreateBucket(BucketName)
    VerSonEnable(BucketName)
    LifeCycle_Mgmt(BucketName,TransDays,NonCrV,ExpDays)


