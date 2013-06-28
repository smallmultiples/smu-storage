from django.contrib.staticfiles.storage import StaticFilesStorage
from pipeline.storage import PipelineMixin
from storages.backends.s3boto import S3BotoStorage

class S3PipelineStorage(PipelineMixin, S3BotoStorage):
    pass

class PipelineStorage(PipelineMixin, StaticFilesStorage):
    pass