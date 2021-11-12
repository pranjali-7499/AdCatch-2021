from django.db import models
from django.db.models import FileField 

# Create your models here.

class Upload_File(models.Model):
    videoname = models.CharField(max_length=100, default="")
    videotype = models.CharField(max_length=100, default="")
    filename = FileField(upload_to="default_storage", null=True)

    def __str__(self):
        return self.videoname