import boto3

def LifeCycle_Mgmt(BucketName)
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
                            'Days': 90,
                            'StorageClass': 'STANDARD_IA'
                        },
                    ],
                    'NoncurrentVersionTransitions': [
                        {
                            'NoncurrentDays': 90,
                            'StorageClass': 'GLACIER'
                        },
                    ],
                    'NoncurrentVersionExpiration': {
                        'NoncurrentDays': 91
                    }
                },
            ]
        }
    )