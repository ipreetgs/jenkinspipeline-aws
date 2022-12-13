import sys
import boto3
BucketName = sys.argv[1]
ExpDay = int(sys.argv[2])
TransDay = int(sys.argv[3])
oth = int(sys.argv[4])



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
        # ExpectedBucketOwner=''
    )

LifeCycle_Mgmt(BucketName,ExpDay,TransDay,oth)