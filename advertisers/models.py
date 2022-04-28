from django.db import models

class Client(models.Model):
    """
    Assignee : 홍은비
    Reviewer : -
    """
    class Meta:
        db_table = 'client'

    name = models.CharField(max_length=100)