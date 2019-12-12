## Golden AMI Pipeline

This repo contains resources for building a Golden AMI Pipeline with AWS Marketplace, AWS Systems Manager, Amazon Inspector, AWS Config, and AWS Service Catalog.

This work is based on architectures described in the following content. 
1. [Building a Secure, Approved AMI Factory Process Using Amazon EC2 Systems Manager (SSM), AWS Marketplace, and AWS Service Catalog](https://d1.awsstatic.com/whitepapers/aws-building-ami-factory-process-using-ec2-ssm-marketplace-and-service-catalog.pdf)

1. [How to Set Up Continuous Golden AMI Vulnerability Assessments with Amazon Inspector](https://aws.amazon.com/blogs/security/how-to-set-up-continuous-golden-ami-vulnerability-assessments-with-amazon-inspector/)

Here is a link to the Step-By-Step instructions guide for this work - [Golden-AMI-Pipeline-Guide V1.0.pdf](https://github.com/aws-samples/aws-golden-ami-pipeline-sample/blob/V-1.0/Golden-AMI-Pipeline-Guide%20V1.0.pdf)

Note - The GitHUB repo is currently not available for external commits/pull requests.

## License

This library is licensed under the MIT-0.


## Observations:
 - Mismatch in the actual inspector report and the values stored in the parameter store  [FIXED]
 - What are the hard code iam account # in InspectorCompleteTopicPolicy  [These are required for inspector to sent the notifications. https://docs.aws.amazon.com/inspector/latest/userguide/inspector_assessments.html]
 - Inspector doesn't support SLE [There is already a request to support SLE]

 - Instructions to create the portfolio are off as the UI have changed. [ update the documentatiion]
    ```
        In the child/recieving acc, a new portfolio have to be created and them the shared product have to be imported.
        Then create the launch contrains 
        Add the user a.k.a the childuser
    ```
        
 
## Nice to Have
 - Support for encrypted AMI [ Work in progress]
    * images encrypted with AWS managed keys cannot be shared
     - to support this, a predefined cmk shared child accounts 
     - 
    * YAML version of the templates [ use the cfn-flip tool and test ]


 - Notifications on failures [ DONE for the ami doc ]
    * Add lambda
    * Add role
    * Add a sns Topic
    * Add subscription to the sns topic
    * analyse the ones that says "proceed on failure" | Great if there can be 2 things that can be invoked in case of a failure


 
 - Convert to a nested stack | Separate the network part template
 - Put Parameter to avoid filling them before launching


## Validate
 - End to End , as-is flow 
 - Validate the config to flag non-compliant EC2 instances [NEW VERSION AVAILABLE]
 - custom scripts for the pre and post update [DONE]
     -- upload a shell script to an s3 bucket, make it public read [DONE]



Things fixed:
 - inspector results in the main flow and continuous pipeline
 - compliance flow [new changes]
 - the included and excluded packages

 - Delete instances after continous compliance test [will not do for now, but this is a remediation in config]
 - Change the platform type to just LINUX for the ssm document [NOT Started]

### Supporting Encryption:
 - AutomationServiceRole - have access to the cmk's of all region to build the ami
 - Lambda functions (copy to multiple region and accounts need to have access to the cmk)

 - Every source region will have a cmk 
 - the target acc's iam/role will have access to the src cmk's in all the regions. [without access user will not be able to launch an instance]
 - pass a JSON to map regions and the cmk for every acc.
 - New flow:
      -- encrypted ami is build in the src acc's src region by the doc1
      -- share ami doc, will copy the ami to the src regions thats defined in the target acc's regions with the cmk in the src region
      -- The lambda function - share-to-mulitple-accounts will share the ami's from each src region to the target regions.
      -- All these cmk's MUST BE ALREADY shared with the target acc's iam user or the role.

{"us-east-1": "ff214fd2-000f-4070-8ca9-0c4719a858e8","us-east-2": "af974333-3ea5-490b-9362-b5bd3a381861","us-west-1": "bdefbc01-0d35-4781-8e47-ee7298b83e1b","us-west-2": "2feeb89f-c904-485c-9fcf-4da0aa9a86e3"}


{\"us-east-1\": \"883dc4ba-46e8-4878-9fa4-4609919def7e\",\"us-east-2\": \"870b8dee-313c-4af8-b53b-2c995db14025\",\"us-west-1\": \"3c71c680-f31e-4f9e-be1c-9af0d4717aa3\",\"us-west-2\": \"ec0bfa3b-b5a7-46bb-9002-dc9115d2cd1b\"}