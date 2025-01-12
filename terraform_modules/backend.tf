terraform {
  backend "s3" {
    bucket         = "purandhar-s3-890" # change this
    key            = "terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-lock"
  }
}