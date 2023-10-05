import boto3

def delete_instance(i-986345c789aef8):
    #deletion

    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(i-986345c789aef8)
    instance.terminate()

    print(f'Instance {i-986345c789aef8} terminated.')
