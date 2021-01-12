"""apa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

admin.site.site_header = "Ayurveda Proctology Admin"
admin.site.site_title = "Ayurveda Proctology Admin Portal"
admin.site.index_title = "Ayurveda Proctology Portal"

from django.urls import path, include
from home.views import views
from django.conf import settings
from accounts.views import registration_view, logout_view, login_view, account_view, AccountList
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from accounts.views import AccountList

app_name = 'apa'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('events/', include('events.urls')),
    path('subscribe/', include('subscribe.urls')),
    path('register/', registration_view, name = "register"),
    path('logout/', logout_view, name = "logout"),
    path('login/', login_view, name = "login"),

    
    path('account/update/', account_view, name='account_update'),
    path('account/details', account_view, name='account_details'),
    
    path('account/list/', AccountList.as_view(), name='account_list'),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), 
        name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),

    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
     name='password_reset_complete'),

] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    