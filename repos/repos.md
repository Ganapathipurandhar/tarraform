# Terraform AWS VPC Creation Workflow
~~~
https://github.com/ministryofjustice/modernisation-platform

https://github.com/techiescamp/terraform-aws.git
~~~
The VPC Terraform code is structured as follows:

```
├── infra
│   └── vpc
│       ├── main.tf
│       └── variables.tf
├── modules
│   └── vpc
│       ├── endpoint.tf
│       ├── internet-gateway.tf
│       ├── nacl.tf
│       ├── nat-gateway.tf
│       ├── outputs.tf
│       ├── route-tables.tf
│       ├── subnet.tf
│       ├── variables.tf
│       └── vpc.tf
└── vars
    └── dev
        └── vpc.tfvars
```

- The `vars` folder contains the variables file named `vpc.tfvars`. It is the only file that needs modification.
- The `modules/vpc` folder contains the following VPC-related resources. All resource provisioning logic is part of these resources:
  - `endpoint`
  - `internet-gateway`
  - `nacl`
  - `nat-gateway`
  - `route-tables`
  - `subnet`
  - `vpc`
- The `infra/vpc/main.tf` file calls the VPC module with all the VPC resources using the variables passed through the `vpc.tfvars` file.

## Create VPC Using Terraform

**Note:** The VPC and subnets for this demo are created based on our VPC design document. Please refer to it if you want to understand how to design a VPC.

We will create the VPC with the following specifications:

- **CIDR Block:** `10.0.0.0/16`
- **Region:** `us-west-2`
- **Availability Zones:** `us-west-2a`, `us-west-2b`, `us-west-2c`
- **Subnets:** 15 Subnets (one per availability zone)
  - Public Subnets (3)
  - App Subnets (3)
  - DB Subnets (3)
  - Management Subnets (3)
  - Platform Subnets (3)
- **NAT Gateway** for private subnets
- **Internet Gateway** for public subnets
- **Enabled Endpoints:** S3, CloudWatch, and Secrets Manager
- **Dedicated NACLs** for 4 sets of subnets