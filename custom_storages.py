from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storag


class CustomS3Boto3Storag(S3Boto3Storag):
    location = settings.AWS_MEDIA_LOCATION
