from django.db import models


class Client(models.Model):
    PLANS = (
        ('M', 'Plano Mensal'),
        ('T', 'Plano Tri mestral'),
        ('A', 'Plano Anual')
    )
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=15)
    website = models.URLField()
    plan = models.CharField(max_length=1, choices=PLANS)
