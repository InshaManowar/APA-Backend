from django.shortcuts import render,redirect
from django.contrib import admin
from django.urls import path, include
from apa import views
from .import views
from django.conf.urls.static import static
from django.conf import settings
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from events.models import Event
from django.template.loader import render_to_string

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Gallery, GalleryImage, VideoDisplay, Video, VideoSidebar
# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def get_context_data(self, *args, **kwargs):
    context['myVar'] = True
    return context


def aboutus(request):
    return render(request, 'home/aboutus.html')



def visions(request):
    return render(request, 'home/visions.html')



def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Subject Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'], 
			    'last_name': form.cleaned_data['last_name'], 
			    'email': form.cleaned_data['email_address'], 
			    'message':form.cleaned_data['message'], 
                }
            message = "\n".join(body.values())
            recepient = str(form['email_address'].value())

            try:
                send_mail(subject, message, recepient, ['isterecruitments2020@gmail.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("home:home")
    
    form = ContactForm(request.POST)
    return render(request, "home/contactus.html", {'form':form})

def home_screen_view(request):
    context = {}
    
    query = ""
    
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)
        
    event_list = sorted(get_blog_queryset(query), key = attrgetter('date_updated'), reverse=True)
    context['event_list']= event_list
    
    return render(request, "home/aboutus.html", context)

 

def gallery_view(request):
    photos = GalleryImage.objects.all()
    paginator = Paginator(photos, 2)
    page = request.GET.get('page')
    try:
        image_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        image_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        image_list = paginator.page(paginator.num_pages)
    return render(request, 'home/gallery.html', {
        'photos':photos,
        'image_list':image_list
        
    })
def video_view(request):
    video = VideoDisplay.objects.all()
    video_side = VideoSidebar.objects.all()
    return render(request, 'home/video.html',{ 'video': video, 'video_side' : video_side })
