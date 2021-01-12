from django.contrib import admin
from .models import Event, EventImage, EventTable
# Register your models here.
class EventImageAdmin(admin.StackedInline):
    model = EventImage
 
class EventTableAdmin(admin.StackedInline):
    model = EventTable
 
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'startdate','enddate')  #displays the tuple for each post
    list_filter = ("status",) #filters based on status
    search_fields = ['title','content','startdate'] #search bar 
    prepopulated_fields = {'slug': ('title',)}  #prepopulated_fields populates the slug, now if you create a post the slug will automatically be filled based upon your title.
    inlines = [EventImageAdmin,EventTableAdmin]
    
@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):
    pass
@admin.register(EventTable)
class EventTableAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin) 
