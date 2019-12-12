import boto3

client = boto3.client('ec2', 'us-west-2')

response = client.copy_image(
    # ClientToken='string',
    # Description='string',
    Encrypted=True,
    KmsKeyId='ec0bfa3b-b5a7-46bb-9002-dc9115d2cd1b',
    Name='manual-python-script-based-copied',
    SourceImageId='ami-0e7a6b4ed4c4adcf1',
    SourceRegion='us-east-2',
    DryRun=False
)