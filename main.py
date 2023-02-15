import boto3
import sys
from AwsLib import AwsServices

ServCreate=[]
for i, arg in enumerate(sys.argv[1:]):
    ServCreate.append(arg)

for i in ServCreate:

    print(f"Creating {i} in AWS")
    try:
            
        if i.lower() =="ec2":
            input("Enter ec2 specification")
            print("created EC2")
            # AwsServices.create_instance()
        elif i.lower() =="s3":
            BucketName=input("enter bucket name")
            print("created S3")
            s3 = boto3.resource('s3')
            AWS_buckets = [bucket.name for bucket in s3.buckets.all()]
            if BucketName in AWS_buckets:
                print("Bucket already avaliable")
            else:
                print("name not found: Creating one!!!!!!")
                AwsServices.CreateBucket(BucketName)
                AwsServices.VerSonEnable(BucketName)
                AwsServices.LifeCycle_Mgmt(BucketName,35,40,45)
        elif i.lower() =="budget":
            input("enter budget name")
            print("created AWS Budgets")
        elif i.lower() =="other":
            print("created ")
        else:
            print("Not Valid Service ")
    except Exception as E:
        print(f"error in input, {E}")



