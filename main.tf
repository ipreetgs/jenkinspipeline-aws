locals {
  bucketName=var.BucketName
}
provider "aws" {
  region = "us-east-1"
  shared_credentials_files = ["/credentials"]
  profile = "demo"
}

resource "aws_s3_bucket" "b" {
  bucket = local.bucketName
  versioning {
    enabled=True
  }

  tags = {
    Name        = "My bucket"
    Environment = "test"
  }
}
