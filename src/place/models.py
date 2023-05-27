from django.db import models
from django.urls import reverse
from location_field.models.plain import PlainLocationField
from ..user.models import User


class Place(models.Model):
    """Place"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='places', verbose_name='Id создателя')
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    location = PlainLocationField(zoom=7)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('show_place', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-id']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
