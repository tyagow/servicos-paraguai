from django.db import models
from _datetime import datetime


class Service(models.Model):
    client = models.ForeignKey('core.Client')
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=50)
    logo = models.ImageField()
    valid_until = models.DateTimeField(default=datetime.now())
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    category = models.ForeignKey('Category', null=True)


class Category(models.Model):
    parent = models.ForeignKey('self', null=True)
    name = models.CharField(max_length=60)
    logo = models.ImageField()
