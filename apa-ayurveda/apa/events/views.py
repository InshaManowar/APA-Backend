from django.shortcuts import render,get_object_or_404

from django.views import generic
from .models import Event, EventImage, EventTable


# Create your views here.

class EventList(generic.ListView):
    paginate_by = '9'
    queryset = Event.objects.filter(status=1).order_by('startdate')
    template_name = 'events/index.html'

class EventDetails(generic.DetailView):
    model = Event
    template_name= 'events/events.html'

def detail_view(request, slug):
    event = get_object_or_404(Event, slug=slug)
    photos = EventImage.objects.filter(event=event)
    table = EventTable.objects.filter(event=event)
    return render(request, 'events/events.html', {
        'event':event,
        'photos':photos,
        'table':table
        
        })
    
    