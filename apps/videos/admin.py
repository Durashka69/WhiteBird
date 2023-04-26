from django.contrib import admin
from django.utils.html import format_html
from .models import Video, Image


class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'video_preview', 'date_created', 'date_updated')
    readonly_fields = ('video_preview', 'video_compressed', 'compressed_video_url')

    def video_preview(self, obj):
        if obj.compressed_video_url:
            return format_html(
                f'<video width="320" height="240" controls><source src="{obj.compressed_video_url}" type="video/mp4"></video>'
            )
        else:
            return "No compressed video available."

    video_preview.short_description = 'Compressed Video Preview'


admin.site.register(Video, VideoAdmin)
admin.site.register(Image)
