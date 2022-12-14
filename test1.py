import boto3
def LifeCycle_Mgmt(BucketName,TransDays,NonCrV,ExpDays):
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