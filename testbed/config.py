import boto3
import json

region = 'us-west-1'
client = boto3.client('config', region)
ssm = boto3.client('ssm', region)
amis = ssm.get_parameter(Name="/GoldenAMI/latest")['Parameter']['Value']
print(type(amis))
update_ami = {}
update_ami['amiIds'] = amis
json_update_ami = json.dumps(update_ami)
print(json_update_ami)

response = client.put_config_rule(
    ConfigRule={
        'ConfigRuleArn': 'arn:aws:config:us-west-1:811284348584:config-rule/config-rule-suojze',
        'Source': {
            'Owner': 'AWS',
            'SourceIdentifier': 'APPROVED_AMIS_BY_ID',
        },
        'InputParameters': json_update_ami
        # 'MaximumExecutionFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours',
    },
)