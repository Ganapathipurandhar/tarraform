# Terraform Modules in DevOps

## Overview
Using Terraform modules in a DevOps environment allows you to organize and reuse your infrastructure as code. Here are some key concepts and strategies to effectively use Terraform modules and manage their deployment across different development teams.

## Setting Up Terraform Modules

### Define and Use a Module
Define a module in a separate directory and use it in your main configuration:

```hcl
# Define a module in a file (e.g., modules/ec2/main.tf)
module "ec2_instance" {
  source = "./modules/ec2"

  instance_name = "my-ec2-instance"
  instance_type = "t2.micro"
}
```

### Example of Using Multiple Instances of the Module
To create multiple EC2 instances using the same module, ensure each module block has a unique name:

```hcl
module "EC2_instance_1" {
  source = "github.com/your-repo/terraform-modules//path-to-module"

  instance_name = "Instance 1"
  instance_type = "t2.micro"
}

module "EC2_instance_2" {
  source = "github.com/your-repo/terraform-modules//path-to-module"

  instance_name = "Instance 2"
  instance_type = "t2.micro"
}
```

## Workflow for Development Teams

### Branching Strategy
Each development team should follow these steps:

1. **Create a Branch**: Use `git checkout -b <dev-team-branch>` to create a new branch.
2. **Configure the Module**: Add or modify Terraform configuration files.
3. **Commit Changes**: Commit changes to the branch.

```sh
git checkout -b dev-team-branch
terraform init
terraform plan
git add .
git commit -m "Added EC2 instance for Team"
git push origin dev-team-branch
```

### Merge Process
Once changes are tested and validated:

1. **Create a Pull Request (PR)**: Submit a PR to merge the branch into the main branch.
2. **Code Review**: Review and approve the PR.
3. **Merge to Main**: Merge the branch into the main branch.
4. **Apply Changes**: Apply the changes in the main environment.

```sh
git checkout main
git merge dev-team-branch
terraform apply
```

## Restricting Terraform Apply

### Preventing Direct Apply in Dev Branches
To prevent developers from running `terraform apply` in their dev branches:

- Use **Policy as Code** (Sentinel/OPA)
- **Branch Protection Rules**
- **CI/CD Pipeline Restrictions**
- **Pre-Commit Hooks**
- **Environment Variables**

### Example CI/CD Pipeline Configuration Using GitHub Actions

```yaml
name: Terraform Apply

on:
  push:
    branches:
      - main

jobs:
  apply:
    runs-on: self-hosted  # Ensure this refers to your VM
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v1

      - name: Terraform Init
        run: terraform init

      - name: Terraform Apply
        run: terraform apply -auto-approve
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
```

## Permissions for Developers

Grant developers the necessary permissions to run `terraform init` and `terraform plan`:

### Example IAM Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::your-s3-bucket",
        "arn:aws:s3:::your-s3-bucket/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:Scan",
        "dynamodb:Query",
        "dynamodb:DescribeTable"
      ],
      "Resource": "arn:aws:dynamodb:us-west-2:123456789012:table/terraform-locks"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeSubnets",
        "ec2:DescribeVpcs"
      ],
      "Resource": "*"
    }
  ]
}
```

## Summary
By following these practices, development teams can effectively collaborate on Terraform modules while maintaining control and security over the infrastructure provisioning process.
