#Launching an Ec2 Instance

import boto3

def launch_instance\
                (ami='ami-067d1e60475437da2',
                    instance_type='t2.micro',
                    key_name='AWSbigdata',
                    group_name='AWSbigdata',
                    ssh_port=32,
                    cidr='0.0.0.0/0',
                    tag='AWSbigdata',
                    user_data=None,
                    login_user='ec2-user'):

    ec2 = boto3.resource('ec2')

    key_pairs = ec2.key_pairs.filter(KeyNames=[key_name])
    if not list(key_pairs):
        print(f'Creating key pair: {key_name}')
        key_pair = ec2.create_key_pair(KeyName=key_name)
        with open(f'{key_name}.pem', 'w') as key_file:
            key_file.write(key_pair.key_material)
