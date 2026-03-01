terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.1"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "random_pet" "bucket_name" {
  prefix = "my-trading-app-bucket"
  length = 4
}

resource "aws_s3_bucket" "example_bucket" {
  bucket = random_pet.bucket_name.id
  acl    = "private"
}
