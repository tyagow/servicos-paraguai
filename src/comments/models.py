from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class CommentManager(models.Manager):
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id).filter(aprovado=True)
        return qs


class Comment(models.Model):
    nome = models.CharField(max_length=60)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    conteudo = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=False)

    objects = CommentManager()

    def __str__(self):
        return self.nome