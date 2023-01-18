import boto3
from datetime import datetime
def LifeCycle_Mgmt(BucketName,TransDay,ExpDay,NonCurrVeTrans):
    s3=boto3.resource('s3')
    bucket_lifecycle_configuration=s3.BucketLifecycleConfiguration(BucketName)
    response = bucket_lifecycle_configuration.put(
        ChecksumAlgorithm='CRC32',
        LifecycleConfiguration={
            'Rules': [
                {
                    'Expiration': {
                        'Days': ExpDay,
                        'ExpiredObjectDeleteMarker': True
                    },
                    'ID': 'demotxchdrule',
                    'Prefix': '',
                    'Filter': {
                        
                    },
                    'Status': 'Enabled',
                    'Transitions': [
                        {
                            'Days': TransDay,
                            'StorageClass': 'STANDARD_IA'
                        },
                    ],
                    'NoncurrentVersionTransitions': [
                        {
                            'NoncurrentDays': NonCurrVeTrans,
                            'StorageClass': 'GLACIER',
                        },
                    ],
                    'NoncurrentVersionExpiration': {
                        'NoncurrentDays': 123,
                    },
                },
            ]
        },
    )
LifeCycle_Mgmt("demotxchd1",15,20,30)