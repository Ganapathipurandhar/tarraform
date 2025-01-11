# Terraform
* Terraform is an Infrastructure as Code(IaC) tool developed by HashiCorp by HCL language
    1) IaC involves managing infrastructure programmatically, reducing manual efforts, repeated tasks and errors(by UI it will take minutes to create service --> by IAC it will seconds by API AS CODE--> we can create 100's of services without delay)
    2) Universally applicable to multiple cloud providers like AWS, Azure,GCP etc (hcl template(yml file) convented to the **API AS CODE as aws api, azure api etc** this api's create Infrastructure )

_____________________________________________________________________________________________________________________________________

# Install Terraform

## Windows

1. Install Terraform from the Downloads [Page](https://developer.hashicorp.com/terraform/downloads)

2. Use GitHub Codespaces (Free for 60 hours per month) or vs code or any IDE

- Login to your GitHub account
- Click on the Profile Icon to the top right
- Click on "your codespaces" as shown in the [Image](../Images/codespaces-location.png)
- Codespaces will provide you a virtual machine with Ubuntu and VS Code by default.
- Follow the steps provided in the Downloads [Page](https://developer.hashicorp.com/terraform/downloads) for Linux.

## Linux
- Follow the steps provided in the Downloads [Page](https://developer.hashicorp.com/terraform/downloads) for Linux.
## macOS
- Follow the steps provided in the Downloads [Page](https://developer.hashicorp.com/terraform/downloads) for macOS.

__________________________________________________________________________________________________________________________________
## aws
* install **awscli** and configure aws cli [aws configure] and add aws key's
## azure
install **azure cli** --> az login -->A browser window will open to authenticate your credentials-->(az account set --subscription <subscription-id> or az account list --output table )
--> For automation, secure Service Principal credentials in tools like Azure Key Vault, environment variables, or CI/CD secret stores.
------------------------------------------------------------------------------------------------------------------------------------

## Initialize Terraform**

In your terminal, navigate to the directory containing your Terraform configuration files and run:

```
terraform init
```

This command initializes the Terraform working directory, downloading any necessary provider plugins.

## Terraform plan
~~~
terraform plan
~~~
this shows what are the resources will create(like a dry-test)

## Apply the Configuration

Run the following command to create the AWS resources defined in your Terraform configuration:

```
terraform apply
```

Terraform will display a plan of the changes it's going to make. Review the plan and type "yes" when prompted to apply it.


## Destroy Resources

If you want to remove the resources created by Terraform, you can use the following command:

```
terraform destroy
```

Be cautious when using `terraform destroy` as it will delete resources as specified in your Terraform configuration.

## Command	Description
**terraform init**  Initializes the working directory.

**terraform plan**	Previews the changes Terraform will make.

**terraform apply**	Applies the changes to the infrastructure.

**terraform destroy**	Destroys all resources managed by the current configuration.

**terraform validate**	Validates the syntax of the configuration files.

**terraform fmt**	Formats the configuration files to the standard style.


