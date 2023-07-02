from django.db import models

class proxyModel(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    protocol = models.CharField(max_length=255, default='')

class proxyCountryModel(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    country = models.CharField(max_length=255, default='')
    local_time = models.TimeField()
    
    