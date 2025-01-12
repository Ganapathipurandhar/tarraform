provider "aws" {
  region = "us-east-1"
}

# Module instance for 'dev_env'
module "aws_ec2instances_dev_env" {
  source              = "./modules/aws_ec2instances"
  aws_iam             = "ami-05576a079321f21f8"
  aws_instance_type   = "t2.micro"
  aws_subnet_id       = "subnet-002dd57311d7a190b"
  tag_name            = "dev_env"
  kp                  = "web01key"
}

