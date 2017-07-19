from __future__ import unicode_literals

from random import randint

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Count
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from markdown_deux import markdown

from src.comments.models import Comment
from src.posts.utils import get_read_time


class PostManagerQuerySet(models.QuerySet):
    def active(self):
        return self.filter(draft=False).filter(publish__lte=timezone.now())

    def noticias(self):
        return self.active().filter(type=0).order_by('-timestamp')

    def lazer(self):
        return self.active().filter(type=1).order_by('-timestamp')

    def principais(self, count=None):
        total = self.count()
        if total == 0:
            return []
        if not count:
            return self.order_by('-timestamp')
        elif count > total:
            dif = count - total
            principais = list(self.all().order_by('-timestamp'))
            while dif > 0:
                index = self.aggregate(count=Count('id'))['count']
                random_index = randint(0, index - 1)
                principais.append(self.all()[random_index])
                dif -= 1

            return principais
        else:
            return self.order_by('-timestamp')[:count]


PostManager = models.Manager.from_queryset(PostManagerQuerySet)

TIPO_POST_CHOICES = getattr(settings, 'TIPO_POST_CHOICES', (
    (0, ("Noticia")),
    (1, ("Lazer Turismo")),
))


def upload_location(instance, filename):
    # filebase, extension = filename.split(".")
    # return "%s/%s.%s" %(instance.id, instance.id, extension)
    PostModel = instance.__class__
    # new_id = PostModel.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object, 
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" % (instance.slug, filename)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              help_text='### ATENÇÃO - TAMANHO DA IMAGEM PRECISA SER 555x235 NOTICIA OU 265x360 PARA LAZER / TURISMO ###'
                              )
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    read_time = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    type = models.SmallIntegerField(("categoria"), choices=TIPO_POST_CHOICES, default=0)

    objects = PostManager()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("noticias:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]

    def get_markdown(self):
        content = self.content
        markdown_text = markdown(content)
        return mark_safe(markdown_text)

    @property
    def comments(self):
        qs = Comment.objects.filter_by_instance(self)
        return qs

    @property
    def get_content_type(self):
        qs = ContentType.objects.get_for_model(self.__class__)
        return qs


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    if instance.content:
        html_string = instance.get_markdown()
        read_time = get_read_time(html_string)
        instance.read_time = read_time

# before save a post this signal is triggered
pre_save.connect(pre_save_post_receiver, sender=Post)

