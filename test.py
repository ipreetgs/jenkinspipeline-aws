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
                        'Date': datetime(2015, 1, 1),
                        'Days': ExpDay,
                        'ExpiredObjectDeleteMarker': True
                    },
                    'ID': 'demotxchdrule',
                    'Prefix': 'string',
                    'Filter': {
                        'Prefix': 'string',
                        'Tag': {
                            'Key': 'string',
                            'Value': 'string'
                        },
                        'ObjectSizeGreaterThan': 123,
                        'ObjectSizeLessThan': 123,
                        'And': {
                            'Prefix': 'string',
                            'Tags': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ],
                            'ObjectSizeGreaterThan': 123,
                            'ObjectSizeLessThan': 123
                        }
                    },
                    'Status': 'Enabled',
                    'Transitions': [
                        {
                            'Date': datetime(2015, 1, 1),
                            'Days': TransDay,
                            'StorageClass': 'STANDARD_IA'
                        },
                    ],
                    'NoncurrentVersionTransitions': [
                        {
                            'NoncurrentDays': NonCurrVeTrans,
                            'StorageClass': 'GLACIER',
                            'NewerNoncurrentVersions': 123
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
    )
LifeCycle_Mgmt("demotxchd1",15,20,30)