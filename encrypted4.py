import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('antotest1')
for obj in bucket.objects.all():
    key = s3.Object(bucket.name, obj.key)
    print "Encryption State:", key.server_side_encryption,":and:"  ,"Bucket name is:", bucket.name
