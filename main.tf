locals {
  bucketName=var.BucketName
}
provider "aws" {
  region = "us-east-1"
  shared_credentials_files = ["/credentials"]
  profile = "demo"
}

resource "aws_s3_bucket" "bucket" {
  bucket = local.bucketName
  versioning {
    enabled=true
  }
  
  acl = "private"
  tags = {
    Name        = "My bucket"
    Environment = "test"
  }
}
resource "aws_s3_bucket_lifecycle_configuration" "bucket-config" {
  bucket=aws_s3_bucket.bucket.bucket
  rule {
    id = "demorule"

    filter {}

    transition {
      days          = 30
      storage_class = "STANDARD_IA"
    }

    transition {
      days          = 60
      storage_class = "GLACIER"
    }

    status = "Enabled"
  }
    
}