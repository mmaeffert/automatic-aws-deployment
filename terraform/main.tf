provider "aws" {
  region     = "eu-central-1"
  access_key = var.access_key
  secret_key = var.secret_key
}

# Define an S3 bucket resource
resource "aws_s3_bucket" "example_bucket" {
  bucket = var.bucket_name # Bucket Name
  force_destroy = var.force_destroy
}
