from django.db import models
from cloudinary.models import CloudinaryField


class Video(models.Model):
    video = CloudinaryField(
        resource_type='video',
        format='mp4',
        max_length=255
    )
    video_compressed = models.BooleanField(default=False)
    compressed_video_url = models.URLField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.video.name} ({self.date_created})"

    def __str__(self):
        return str(self.video)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
