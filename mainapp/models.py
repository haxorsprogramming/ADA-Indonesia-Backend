from django.db import models

# Create your models here.
class dataPost(models.Model):
    cover = (('Yes', 'Yes'), ('No', 'No'))
    judul = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    short_deks = models.TextField()
    long_deks = models.TextField()
    cover_homepage = models.CharField(max_length=100, choices=cover)
    img_feature = models.CharField(max_length=255)
    writer = models.CharField(max_length=255)
    class Meta:
        db_table = "tbl_post"