from django.db import models

class SelectLanguage(models.Model):
    language=models.CharField(max_length=200)
    topic=models.CharField(max_length=200)
