provider "aws" {
  region = "us-east-1" # Set your desired AWS region
}

resource "aws_instance" "example" {
  ami           = "ami-05576a079321f21f8" # Specify an appropriate AMI ID
  instance_type = "t2.micro"
  subnet_id     = "subnet-002dd57311d7a190b"
  key_name      = "web01key"
  tags = {
    Name = "my-ec2-instance"
  }
}

