import boto3

aws_access_key_id = 'AKIASTXILTBQYT7YPFIL'
aws_secret_access_key = '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'
region_name = 'us-west-2'

s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  region_name=region_name)

bucket_name = 's3-training1'
