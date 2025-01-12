provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "test" {
  ami           = var.aws_iam
  instance_type = var.aws_instance_type
  subnet_id     = var.aws_subnet_id
  key_name      = var.kp

  tags = {
    Name = var.tag_name
  }
}

