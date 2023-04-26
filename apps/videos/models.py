from django.db import models
from cloudinary.models import CloudinaryField

from uuid import uuid4


def generate_filename(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{str(uuid4())}.{ext}"
    return f"{filename}"


class Video(models.Model):
    # video = CloudinaryField(
    #     resource_type='video',
    #     format='mp4',
    #     max_length=255
    # )
    video = models.FileField(upload_to='videos/', max_length=255)
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


class Image(models.Model):
    # img = CloudinaryField(
    #     "image",
    #     blank=False,
    #     null=False,
    # )
    img = models.ImageField(
        verbose_name="Картинка", 
        blank=True, 
        null=True, 
        upload_to=generate_filename
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.img)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
