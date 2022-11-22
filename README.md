## README

Welcome everyone to this tutorial. This repo is intended to show newcomers to our awesome Twinter how AWS works and how to write scripts to interact with it using the boto3 library in Python.

# Setup

-sudo apt get install python3

-sudo apt get install python3-pip

-pip install boto3

# Usage

First we need to create the credenntials file with: touch ~/.aws/credentials

Then, fire up your preferred file editor and copy this into the file (replace the values with the ones given in the e-mail with "Welcome to Twinter" as subject):

[default]

aws_access_key_id = YOUR_KEY

aws_secret_access_key = YOUR_SECRET

So now we can start interacting with AWS. For instance this is what we would need to use to list all of the S3 buckets you have been given access to:

import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)
    
In order for this to work, your user needs permissions, but don't worry about having to ask for more privileges, you are already given a privileged user :)

In case you want to get more info about this, check out the official docs: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
