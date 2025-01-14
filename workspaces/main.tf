provider "aws" {
    region = "us-west-2"
}
variable "instance_type" {
  description = "value"
  type = map(string)
default = {
  "dev"  ="t2.micro"
  "stage"="t2.small"
  "prod" = "t2.xlarge"
}
}

module "aws_ec2instances" {
    source  ="./modules/aws_ec2instances"
    aws_iam             = "ami-05576a079321f21f8"
    aws_instance_type   = lookup(var.instance_type,terraform.workspace,"t2.micro")
    aws_subnet_id       = "subnet-002dd57311d7a190b"
    tag_name            = "dev_env"
    kp                  = "web01key"
}


