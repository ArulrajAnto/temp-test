import boto3
client = boto3.client('s3')
response = s3.get_bucket_encryption(Bucket="lambda-vishal")
count = 0
for i in response['ApplyServerSideEncryptionByDefault']:
    if(i['Encrypted']==True):
        print i['SSEAlgorithm']
        count += 1
if count == 0:
    print "No Volume is Encrypted"
