
from django.db import models
from django.dispatch import receiver
from datetime import datetime

def upload_location(instance, filename, *kwargs):
	file_path = 'home/{gallery}-{filename}'.format(
     gallery=str(instance.gallery), filename=filename)
	return file_path

class Gallery(models.Model):
    title = models.CharField(max_length=250)

 
    def __str__(self):
        return self.title
    
class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to=upload_location, default = None, blank=True)
 
  
class Video(models.Model):
    title = models.CharField(max_length=250)
    created_time = models.DateTimeField( default= datetime.now())

    
    
    def __str__(self):
        return self.title
    
    class Meta:
            ordering = ['-created_time', ]
    
class VideoDisplay(models.Model):
    videos = models.ForeignKey(Video, default=None, on_delete=models.CASCADE)
    display = models.TextField( default = None, blank=True)
 
 
 
    
class VideoSidebar(models.Model):
    videos = models.ForeignKey(Video, default=None, on_delete=models.CASCADE)
    display_sidebar = models.TextField( default = None, blank=True)
 
 
 