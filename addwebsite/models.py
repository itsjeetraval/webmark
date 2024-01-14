
from django.db import models
class Addweb(models.Model):

    web_name = models.CharField(max_length=100)
    web_description = models.TextField()
    web_url = models.URLField(max_length = 200)