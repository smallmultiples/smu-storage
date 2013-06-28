### SMU Storage

SMU Storage is intended to be used with Django-Pipeline and Django-Storages to allow static files and uploaded files to both be sent to the same bucket.

Provides two storage targets, one for uploads and one for static files. By default, static files get sent to `/` and uploaded files get sent to `/uploads/`.

The two storage targets are:

```python
# bucket/
'smu-storage.s3utils.StaticRootS3BotoStorage' 

# bucket/uploads
'smu-storage.s3utils.MediaRootS3BotoStorage' to /uploads.
```

TODO:

Make these be settings:

```python
SMU_STORAGE_STATIC_ROOT # default being '/'
SMU_STORAGE_MEDIA_ROOT # default being '/uploads'
```

Both being paths used in the S3 buckets.