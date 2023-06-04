from django.db import models

class MainInfo(models.Model):
    name_tt = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now_add=True)
