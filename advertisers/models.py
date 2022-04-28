from django.db import models

class Client(models.Model):
    """
    Assignee : 홍은비
    Reviewer : -
    """
    class Meta:
        db_table = 'client'

    client_number = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=32, default=None)
    contact_number = models.CharField(max_length=20, default=None)
    email = models.EmailField(max_length=128, default=None)