import boto3

ec2 = boto3.client('ec2', 'us-east-1')


images= ec2.describe_images(ImageIds=['ami-04875ac4aca3110a7'],DryRun=False)

# response = ec2.run_instances(ImageId='ami-04875ac4aca3110a7',SubnetId='subnet-020ae56c0d4835460',IamInstanceProfile={'Arn':'arn:aws:iam::400646037731:instance-profile/encrypted-golden-ami-ManagedInstanceProfile-1WBQRXOR3PSKF'},SecurityGroupIds=['sg-0eeda5c755bda4388'],InstanceType='t2.small',DryRun=False,MaxCount=1,MinCount=1,TagSpecifications=[{'ResourceType': 'instance','Tags': [{'Key': 'version', 'Value': '0.2'}, {'Key': 'AMI-Type', 'Value': 'Golden'}, {'Key': 'ProductName', 'Value': 'arie-0.1'}, {'Key': 'ProductOSAndVersion', 'Value': 'amz-2019.12'}]}])

print(images['Images'][0])


# ,BlockDeviceMappings=[{'DeviceName':'/dev/sda1','Ebs': {'DeleteOnTermination': True, 'Encrypted': True,'KmsKeyId': '8a688da7-bcbc-435c-8286-ccceefd6a6ff'}}]