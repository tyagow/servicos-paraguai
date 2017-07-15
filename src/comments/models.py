from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _
from star_ratings.models import UserRating


class CommentManager(models.Manager):
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id).filter(aprovado=True)
        return qs

User = settings.AUTH_USER_MODEL


class Comment(models.Model):
    user = models.ForeignKey(User)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    content = models.TextField(_('Conteudo'))
    timestamp = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=False)

    objects = CommentManager()

    def __str__(self):
        return self.user.username

    def get_rate(self):
        return UserRating.objects.for_instance_by_user(self.content_object, user=self.user).score