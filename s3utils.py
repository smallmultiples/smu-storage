from smu_storage import S3PipelineStorage
from django.utils.functional import SimpleLazyObject

StaticRootS3BotoStorage = lambda: S3PipelineStorage(location='')
MediaRootS3BotoStorage  = lambda: S3PipelineStorage(location='uploads')