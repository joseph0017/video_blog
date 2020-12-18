from django.db import models
from django.utils import timezone


# Create your models here.


class Videos(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
    text = models.TextField(max_length = 1000, default = timezone.now)
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'

class Images(models.Model):
        docfile = models.FileField(upload_to='images/')
        title = models.CharField(max_length=100, null = True)
        text = models.TextField(max_length=1000, null = True)
        created_date = models.DateTimeField(default=timezone.now)
        published_date = models.DateTimeField(blank=True, null=True)

        def __str__(self):
            return self.title

        class Meta:
            verbose_name = 'image'
            verbose_name_plural = 'images'






