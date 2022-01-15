from django.contrib import admin
from .models import Song, Events, Team

# Register your models here.
class SongAdmin(admin.ModelAdmin):
    list_display=('title','artist','status','released_on')
    list_filter=("title","artist", "status")
    search_fields=['title','artists']


class EventAdmin(admin.ModelAdmin):
    list_display=('title','location','entry_fee','status')
    list_filter=("title","entry_fee", "location" , "status")
    search_fields=['title','location']
    
admin.site.register(Song,SongAdmin)
admin.site.register(Events, EventAdmin)