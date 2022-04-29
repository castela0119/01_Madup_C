from datetime import date
from django.db import models

from advertisers.models import Client

class Ads(models.Model):
    """
    Assignee : 홍은비
    Reviewer : 김수빈, 진병수
    """
    class Meta:
        db_table = 'ads'

    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)
    platform = models.CharField(max_length=50, default='')
    date = models.DateField(default=date.today)
    cost = models.PositiveIntegerField(default=0)
    impression = models.PositiveIntegerField(default=0)
    click = models.PositiveIntegerField(default=0)
    conversion = models.PositiveSmallIntegerField(default=0)
    cv = models.PositiveBigIntegerField(default=0)