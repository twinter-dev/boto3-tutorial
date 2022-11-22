import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all(): 
    print(bucket.name)

#TODO: change the current password Ecorp!2022&evil for the BBDD to another one.
