from django.db import models


class Alpha(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title