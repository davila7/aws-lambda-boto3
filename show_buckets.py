import boto3
import logging


s3 = boto3.resource('s3')

def lambda_handler(event, context):
    bucketlist = []
    for bucket in s3.buckets.all():
        if bucket.name == "prueba-bucket-aws-cli":
            for objeto_bucket in bucket.objects.all():
                bucketlist.append(objeto_bucket.key)
      
    return {
        "statusCode": 200,
        "body": bucketlist
    }