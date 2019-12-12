import boto3

client = boto3.client('ec2', 'us-east-1')

response = client.run_instances(
    # BlockDeviceMappings=[
    #     {
    #         'DeviceName': '/dev/sda1',
    #         'Ebs': {
    #             'DeleteOnTermination': True,
    #             # 'Iops': 123,
    #             'SnapshotId': 'string',
    #             'VolumeSize': 10,
    #             'VolumeType': 'gp2',
    #             'Encrypted': True,
    #             'KmsKeyId': 'first-role-kms'
    #         },
    #         'NoDevice': 'string'
    #     },
    # ],
    ImageId='ami-09ab4f6d269f2b724',
    InstanceType='t2.small',
    KeyName='aws-mac',
    MinCount=1,
    MaxCount=1,
    Monitoring={
        'Enabled': True
    },
    DryRun=False,
 
    InstanceInitiatedShutdownBehavior='terminate'
)