from django.db import models


class Store(models.Model):
    PLANS = (
        ('F', 'Plano Free'),
        ('M', 'Plano Mensal'),
        ('T', 'Plano Tri mestral'),
    )
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=15)
    website = models.URLField()
    slug = models.SlugField()
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    plan = models.CharField(max_length=1, default='F', choices=PLANS)
    category = models.ForeignKey('Category', null=True)

    class Meta:
        verbose_name = 'Loja'
        verbose_name_plural = 'Lojas'

    def __str__(self):
        return self.name


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name='Categoria', null=True, blank=True)
    name = models.CharField(max_length=60)
    slug = models.SlugField()
    logo = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name
