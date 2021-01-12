from . import views
from django.urls import path

app_name = 'event'
urlpatterns = [
    path('', views.EventList.as_view(), name= 'events'),
    path('<slug:slug>/', views.detail_view, name='details'),

] 
