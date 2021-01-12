
from django.contrib import admin
 
from .models import GalleryImage, Gallery, Video, VideoDisplay, VideoSidebar
 
class GalleryImageAdmin(admin.StackedInline):
    model = GalleryImage
 
class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageAdmin]
 
    class Meta:
       model = Gallery
 
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    pass


admin.site.register (Gallery, GalleryAdmin)

class VideoDisplayAdmin(admin.StackedInline):
    model = VideoDisplay
    

class VideoSidebarAdmin(admin.StackedInline):
    model = VideoSidebar
 
class VideoAdmin(admin.ModelAdmin):
    inlines = [VideoDisplayAdmin, VideoSidebarAdmin]
 
@admin.register(VideoDisplay)
class VideoDisplayAdmin(admin.ModelAdmin):
    pass



admin.site.register (Video, VideoAdmin)