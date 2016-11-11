from django.db import models


class Loja(models.Model):
    PLANS = (
        ('F', 'Plano Free'),
        ('M', 'Plano Mensal'),
        ('T', 'Plano Tri mestral'),
    )
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=15)
    website = models.URLField()
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    plan = models.CharField(max_length=1, default='F', choices=PLANS)
    category = models.ForeignKey('Category', null=True)


class Category(models.Model):
    parent = models.ForeignKey('self', null=True)
    name = models.CharField(max_length=60)
    logo = models.URLField(null=True)
