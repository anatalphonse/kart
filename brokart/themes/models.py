from django.db import models

# Create your models here.
class SiteSettings(models.Model):
        Banner=models.ImageField(upload_to='media/site/')
        Caption=models.TextField()

