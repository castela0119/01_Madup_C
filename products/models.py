from django.db import models

from advertisers.models import Client

class Platform(models.Model):
    class Meta:
        db_table = 'platform'
    
    name = models.CharField(max_length=100)

class ClientPlatform(models.Model):
    class Meta:
        db_table = 'client_platform'
    
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    platform_id = models.ForeignKey(Platform, on_delete=models.CASCADE)

class Ads(models.Model):
    class Meta:
        db_table = 'ads'

    client_platform_id = models.ForeignKey(ClientPlatform, on_delete=models.CASCADE)
    uid = models.CharField(max_length=200)
    date = models.DateField()
    cost = models.IntegerField()
    imporession = models.IntegerField()
    click = models.IntegerField()
    conversion = models.IntegerField()
    cv = models.IntegerField()
    ctr = models.FloatField()
    roas = models.FloatField()
    cpc = models.FloatField()
    cvr = models.FloatField()
    cpa = models.FloatField()