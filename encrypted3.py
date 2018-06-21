import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('antotest')
for obj in bucket.objects.all():
    key = s3.Object(bucket.name, obj.key)
    print key.server_side_encryption
