from django.db import models
from django.utils import timezone


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
    category = models.ForeignKey('Category', null=True, blank=True)

    class Meta:
        verbose_name = 'Loja'
        verbose_name_plural = 'Lojas'
        ordering = ['name']

    def __str__(self):
        return self.name


class CategoryManager(models.Manager):
    def all(self):
        qs = super(CategoryManager, self).filter(parent=None)
        return qs


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name='Categoria', null=True, blank=True)
    name = models.CharField(max_length=60)
    slug = models.SlugField()
    logo = models.URLField(null=True, blank=True)

    objects = CategoryManager()

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name

    def children(self):
        return Category.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True


class Advertisement(models.Model):
    KINDS = (
        ('F', 'Anuncio Free'),
        ('M', 'Anuncio Medio'),
        ('T', 'Anuncio Top'),

    )
    store = models.ForeignKey('Store')
    expires_at = models.DateTimeField()
    website = models.URLField()
    img = models.URLField()
    kind = models.CharField(max_length=1, default='F', choices=KINDS)

    class Meta:
        verbose_name = 'Anúncio'
        verbose_name_plural = 'Anúncios'

    def __str__(self):
        return "{} Anúncio".format(self.store.name)