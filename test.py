import boto3
def LifeCycle_Mgmt(BucketName,TransDay,ExpDay,NonCurrVeTrans):
    s3=boto3.resource('s3')
    bucket_lifecycle_configuration=s3.BucketLifecycleConfiguration(BucketName)
    response=bucket_lifecycle_configuration.put(
        LifecycleConfiguration={
            'Rules': [
                {
                    'Expiration': {
                        'Days': ExpDay,
                        'ExpiredObjectDeleteMarker': True
                    },
                    'ID': 'demorule',
                    'Status': 'Enabled',
                    'Transitions': [
                        {
                            'Days': TransDay,
                            'StorageClass': 'STANDARD_IA',
                        },
                    ],
                    'NoncurrentVersionTransitions': [
                        {
                            'NoncurrentDays': NonCurrVeTrans,
                            'StorageClass': 'GLACIER',
                            'NewerNoncurrentVersions': 2
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
        }
    )
LifeCycle_Mgmt("demotxchd1",15,20,30)