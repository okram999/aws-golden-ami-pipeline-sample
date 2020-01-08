
## Golden AMI Pipeline

  This repo contains resources for building an Encrypted Golden AMI Pipeline with AWS Systems Manager, Amazon Inspector, AWS Config, AWS Key Management Service (KMS) and AWS Service Catalog.

  This work is based on the follow work plus the changes and new feature.
  1. [Building a Secure, Approved AMI Factory Process Using Amazon EC2 Systems Manager (SSM), AWS Marketplace, and AWS Service Catalog](https://d1.awsstatic.com/whitepapers/aws-building-ami-factory-process-using-ec2-ssm-marketplace-and-service-catalog.pdf)

  2. [How to Set Up Continuous Golden AMI Vulnerability Assessments with Amazon Inspector](https://aws.amazon.com/blogs/security/how-to-set-up-continuous-golden-ami-vulnerability-assessments-with-amazon-inspector/)


  3. [Golden AMI pipeline](https://github.com/aws-samples/aws-golden-ami-pipeline-sample) 

  This new solution have the below on top of the above solution:
    * Works with encrypted root volumes
    * Fixed the mismatch in the inspector result on console versus the email notification
    * Added notification on pipeline failure
    * New approach to scan non compliant EC2 instances in the child accounts



## Environmental Setup

  This pipeline can be deployed in any AWS account. But to align to the AWS Landing Zone setup, it may make more sense to be deployed in the shared account. 

  The Encrypted Golden AMI gets created in the shared account and are pushed/shared to the child accounts that will be using the AMI. The child accounts can be the PRODUCTION or NON-PRODUCTION accounts. 

  AMI's with encrypted root volumes are supported. The pipelines will take the keyId for the AWS KMS Customer Master Key IDs. The root volumes for the shared AMI's are re-encypted with the local account's CMK's. This approach will reduce the blast radius in the events of a CMK compromise. 

## Steps:

  1. Log-in to the master account (this is the account where the encrypted golden ami's will be created, NOT the master payer account)
  2. Make sure you have the AWS KMS CMK Id's for all the regions where the AMI will be distributed. Somethings like this in JSON (we will pass this as a parameter later in the Cloudformation template):

              ```{\"us-east-1\": \"b92f5270-745c-c36057afd530\",\"us-east-2\": \"169b24d9-38e6-ad07c3c0750b\",\"us-west-1\": \"bd29dc24-a9dc-53b546986aa0\",\"us-west-2\": \"af85c5bf-0060-e5b1f1138b89\"}```

  3. Create Stack with the template "Gold-AMi-Stack-CFT-CI.json". 
  4. Upload the template "simpleEC2-SSMParamInput.json" to the S3 bucket created from the stack in step #3
  5. Do the below in all the child accounts that will recived the encrypted golden AMI
    * Enable AWS Config, in all the regions where the AMI will be copied to. You can skip any "out of the box" config rules while enabling the service for all resource types
    * Create stack using the tenmplate "Golden-AMI-Cross-Account-Role.json". This will create an IAM role that can be assumed by the master account. As this stack creates IAM role, aws region you select doesn't matter
    * Create stack using the template "Golden-AMI-Compliance-CFT.yml". This stack needs to be created in all regions of the child accounts, where the AMI's will be copied and used.
  6. At this point, we are done setting up the pipelines. To trigger the pipeline: AWS System Manager --> Automation --> Execute automation. Click on the "Owned by me" tab to see the documents that have been created by the pipelines. As the name suggest: 
    * GoldenAMIAutomationDoc - creates the encrypted golden AMI and send it for review
    * CopyAndShareAMI - shares the approved AMI
    * RunContinuousInspection - creates a scheduled scan for the pre-approved ami's
    * DecommisionAMIVersion - decommisions a pre-approved AMI


## Use Case:

  I want to make sure, all my teams are using the approved base images for the AWS EC2 instances. And i want to automate the patching and scanning of the base images. 



## License

  This library is licensed under the MIT-0.
