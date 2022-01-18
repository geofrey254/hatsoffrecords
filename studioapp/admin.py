from django.contrib import admin
from .models import Song, Events, Team, Session

# Register your models here.
class SongAdmin(admin.ModelAdmin):
    list_display=('title','artist','status','released_on')
    list_filter=("title","artist", "status")
    search_fields=['title','artists']


class EventAdmin(admin.ModelAdmin):
    list_display=('title','location','entry_fee','status')
    list_filter=("title","entry_fee", "location" , "status")
    search_fields=['title','location']
    
class SessionAdmin(admin.ModelAdmin):
    list_display=('full_name', 'mobile_number', 'email_address')
    list_filter=('full_name', 'mobile_number', 'email_address')
    search_fields=['full_name', 'mobile_number', 'email_address']
    
admin.site.register(Song,SongAdmin)
admin.site.register(Events, EventAdmin)
admin.site.register(Session, SessionAdmin)