# aws/utils.py

from storages.backends.s3boto3 import S3Boto3Storage
 
def MediaRootS3BotoStorage(): return S3Boto3Storage(location='media_root')
def StaticRootS3BotoStorage(): return S3Boto3Storage(location='static_root')