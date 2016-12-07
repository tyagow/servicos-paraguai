from django.db import models


class CategoryManager(models.Manager):
    def principais(self):
        qs = super(CategoryManager, self).filter(parent=None)
        return qs

    def subcategorias(self):
        return super(CategoryManager, self).filter(parent=self)
