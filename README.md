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
 - What are the hard code iam account # in InspectorCompleteTopicPolicy  [not fixed yet]
 - Inspector doesn't support SLE [There is already a request to support SLE]
 - Instructions to create the portfolio are off as the UI have changed.
    ```
        In the child/recieving acc, a new portfolio have to be created and them the shared product have to be imported.
        Then create the launch contrains 
        Add the user a.k.a the childuser
    ```
        
 
## Nice to Have
 - Support for encrypted AMI
     * images encrypted with AWS managed keys cannot be shared

    * For this to work, the CMK keys needs to be

 - Notifications on failures
    * Add lambda
    * Add role
    * Add a sns Topic
    * Add subscription to the sns topic
    * analyse the ones that says "proceed on failure" | Great if there can be 2 things that can be invoked in case of a failure


 - Yaml version of the files, to support in-line comments
 - Convert to a nested stack | Separate the network part template
 - Put Parameter to avoid filling them before launching


## Validate
 - End to End , as-is flow 
 - Validate the config to flag non-compliant EC2 instances


