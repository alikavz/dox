from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse


class Prod(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now=True)
    price = models.PositiveIntegerField(default=0)  # DecimalField for dollars
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.pk])


class CommentsManager(models.Manager):
    def get_queryset(self):
        return super(CommentsManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    given_stars = [
        ('1', 'horrible'),
        ('2', 'bad'),
        ('3', 'ok'),
        ('4', 'good'),
        ('5', 'perfecto'),
    ]

    prodd = models.ForeignKey(Prod, on_delete=models.CASCADE, related_name='commennnts', )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments', )
    body = models.TextField(verbose_name='text')
    stars = models.CharField(max_length=10, choices=given_stars, verbose_name='rating')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)
    objects = models.Manager()
    cm_manager = CommentsManager()

    def get_absolute_url(self):
        return reverse('detail', args=[self.pk])
