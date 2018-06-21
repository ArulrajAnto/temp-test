#!/usr/bin/env python
import boto3

s3_client = boto3.client('s3')
head = s3_client.head_object(
    Bucket="8kmanagedservicesnvirginia",
    Key="<S3 object key>"
)
if 'ServerSideEncryption' in head:
    print head['ServerSideEncryption']
