import boto3

def rename_instance(i-986345c789aef8, RenameInstance1):

    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(i-986345c789aef8)

    instance.create_tags(Tags=[{'Key': 'AWSbigdata', 'Value': RenameInstance1}])

    print(f'Instance {i-986345c789aef8} renamed to {RenameInstance1}.')

