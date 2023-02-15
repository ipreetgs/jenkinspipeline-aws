import boto3
import botocore

class AwsServices:
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.ec2 = boto3.client('ec2')


    def CreateBucket(self,BucketName):
        self.bucket_name = BucketName
        session = boto3.session.Session()
        s3_client = session.client('s3')
        try:
            self.s3.create_bucket(Bucket=self.bucket_name)
            print(f"S3 bucket '{self.bucket_name}' created successfully.")
        except Exception as E:
            print(E)
            print("some Error in creating bucket")

    def create_bucket(self,bucket_name):
        self.bucket_name = bucket_name
        try:
            self.s3.create_bucket(Bucket=self.bucket_name)
            print(f"S3 bucket '{self.bucket_name}' created successfully.")
        except Exception as e:
            print(f"Error creating bucket: {e}")




    def VerSonEnable(bucket_name):
        resource_for_s3 = boto3.resource("s3", region_name=AWS_REGION)
        versioning = resource_for_s3.BucketVersioning(bucket_name)
        versioning.enable()
        print(f'versioning is enabled for S3 Bucket: {versioning.status}')




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



    def create_instance(self, instance_type, image_id, key_name, security_group_ids, subnet_id):
        self.instance_type = instance_type
        self.image_id = image_id
        self.key_name = key_name
        self.security_group_ids = security_group_ids
        self.subnet_id = subnet_id
        try:
            response = self.ec2.run_instances(
                ImageId=self.image_id,
                InstanceType=self.instance_type,
                KeyName=self.key_name,
                SecurityGroupIds=self.security_group_ids,
                SubnetId=self.subnet_id,
                MinCount=1,
                MaxCount=1
            )
            print(f"EC2 instance created successfully with instance ID: {response['Instances'][0]['InstanceId']}")
        except Exception as e:
            print(f"Error creating EC2 instance: {e}")



    def create_Budget(self,BudgetName):
        self.bucket_name = bucket_name
        try:
            self.s3.create_bucket(Bucket=self.bucket_name)
            print(f"S3 bucket '{self.bucket_name}' created successfully.")
        except Exception as e:
            print(f"Error creating bucket: {e}")






