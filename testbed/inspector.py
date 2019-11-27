import boto3
import time

productOS = "lin"
productName = "httpd"
productVersion = '7'
amiId = 'ami-0b2048ba609342b72'
fullName = amiId+'-'+productOS+'/'+productName+'/'+productVersion
print(f"fullname is: {fullName}")
inspector = boto3.client('inspector','us-west-2')
ssm = boto3.client('ssm','us-west-2')
rules = inspector.list_rules_packages()
instanceId = 'i-08f6c291ffba86d40'

ParamName='/GoldenAMI/'+productOS+'/'+productName+'/'+productVersion+'/latestInstance'
ssm.put_parameter(Name=ParamName,Value=instanceId,Type='String',Overwrite=True)
millis = int(round(time.time() * 1000))
existingTemplates = inspector.list_assessment_templates(filter={'namePattern': amiId+'-'+productOS+'/'+productName+'/'+productVersion})

print("Total length found: "+str(len(existingTemplates['assessmentTemplateArns'])))

# print(existingTemplates)

if len(existingTemplates['assessmentTemplateArns'])==0:
  resGroup = inspector.create_resource_group(resourceGroupTags=[{'key': 'Type','value': amiId+'-'+productOS+'/'+productName+'/'+productVersion}])
  target = inspector.create_assessment_target(assessmentTargetName=fullName,resourceGroupArn=resGroup['resourceGroupArn'])
  template = inspector.create_assessment_template(assessmentTargetArn=target['assessmentTargetArn'],assessmentTemplateName=amiId+'/'+productOS+'/'+productName+'/'+productVersion, durationInSeconds=900,rulesPackageArns=rules['rulesPackageArns'])
  assessmentTemplateArn=template['assessmentTemplateArn']
  print("Template Created: "+template['assessmentTemplateArn'])
  ParamName='/GoldenAMI/'+productOS+'/'+productName+'/'+productVersion+'/assessmentTemplateARN'
  ssm.put_parameter(Name=ParamName,Value=template['assessmentTemplateArn'],Type='String',Overwrite=True)

else:
  assessmentTemplateArn=existingTemplates.get('assessmentTemplateArns')[0]

time.sleep(10)
print("Sleeping......")
run = inspector.start_assessment_run(assessmentTemplateArn=assessmentTemplateArn,assessmentRunName=fullName+"-"+str(millis))
print("run completed")
ParamName='/GoldenAMI/'+productOS+'/'+productName+'/'+productVersion+'/LatestAssessmentRunARN'
ssm.put_parameter(Name=ParamName,Value=run['assessmentRunArn'],Type='String',Overwrite=True)