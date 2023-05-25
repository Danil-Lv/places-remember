from django.db import models
from location_field.models.plain import PlainLocationField
from ..user.models import User


class Place(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='places', verbose_name='Id создателя')
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    location = PlainLocationField(based_fields=['title'], zoom=7)
    slug = models.SlugField(unique=True)
