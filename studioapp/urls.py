from unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
    path('events/', views.events, name='events'),
    path('releases/', views.releases, name='releases'),
    path('booking/', views.booking, name='booking'),
    path('sessions-admin/', views.sessions, name='sessions')
    
   
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)
