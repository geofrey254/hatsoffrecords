from django.shortcuts import render, redirect
from django.core import mail
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from django.views.generic import ListView, DetailView,View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Song, Events, Team
# Create your views here.
def home(request):
    rel = Song.objects.filter(status=1).order_by('-released_on')[0:3]
    event = Events.objects.filter(status=1).order_by('event_date')[0:3]

    context = {
        'rel':rel,
        'event':event
    }
    return render(request, 'studioapp/home.html', context)

def events(request):
    events = Events.objects.filter(status=1).order_by('event_date')
    feature = Events.objects.filter(featured=True).order_by('event_date')[0:3]

    paginator   = Paginator(events, 3)
    page        =   request.GET.get('page')
    try:
        events   =   paginator.page(page)
    except PageNotAnInteger:
        events   =   paginator.page(1)
    except EmptyPage:
        events   =   paginator.page(paginator.num_pages)

    context = {
        'events':events,
        'feature':feature
    }
    
    return render(request, 'studioapp/events.html', context)

def releases(request):
    songs = Song.objects.filter(status=1).order_by('-released_on')
    
    paginator   = Paginator(songs, 3)
    page        =   request.GET.get('page')
    try:
        songs   =   paginator.page(page)
    except PageNotAnInteger:
        songs   =   paginator.page(1)
    except EmptyPage:
        songs   =   paginator.page(paginator.num_pages)
        
    context = {
        'songs':songs
    }
        
    return render(request, 'studioapp/releases.html', context)
    
    