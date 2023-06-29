from django.db import models
from django.urls import reverse


class Alpha(models.Model):
    objects = None
    title = models.CharField(max_length=255, verbose_name='Name')
    content = models.TextField(blank=False, verbose_name='Biography')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Creation time')
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Fraction', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Warcraft heroes'
        verbose_name_plural = 'Warcraft heroes'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('read_data', kwargs={'post_id': self.pk})


class Fraction(models.Model):
    objects = None
    name = models.CharField(max_length=100, db_index=True, verbose_name='Fraction')

    class Meta:
        verbose_name = 'Fractions'
        verbose_name_plural = 'Fractions'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('fraction', kwargs={'cat_id': self.pk})
