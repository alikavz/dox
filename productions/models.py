from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _


class Prod(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateTimeField(default=timezone.now, verbose_name=_('Date of creation'))
    datetime = models.DateTimeField(auto_now=True)
    price = models.PositiveIntegerField(default=0)  # DecimalField for dollars
    status = models.BooleanField(default=True)
    image = models.ImageField(verbose_name=_('image'), upload_to='productions/img/w', blank=True, )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.pk])


class CommentsManager(models.Manager):
    def get_queryset(self):
        return super(CommentsManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    given_stars = [
        ('1', _('horrible')),
        ('2', _('bad')),
        ('3', _('ok')),
        ('4', _('good')),
        ('5', _('perfecto')),
    ]

    prodd = models.ForeignKey(Prod, on_delete=models.CASCADE, related_name='commennnts', )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments', )
    body = models.TextField(verbose_name=_('text'))
    stars = models.CharField(max_length=10, choices=given_stars, verbose_name=_('rating'))
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)
    objects = models.Manager()
    cm_manager = CommentsManager()

    def get_absolute_url(self):
        return reverse('detail', args=[self.prodd.id])
