from django.db import models


class Document(models.Model):
    name = models.CharField(max_length=50)
    docfile = models.FileField(upload_to='documents')
    class_name = models.CharField(max_length=20)
