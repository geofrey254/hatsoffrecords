import sys
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.urls import reverse
from tinymce import models as tinymce_models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

STATUS=(
    (0,"Draft"),
    (1,"Publish")
)

class Song(models.Model):
    title           = models.CharField(max_length=250, null=True)
    artist          = models.CharField(max_length=250, null=True)
    released_on     = models.DateTimeField(auto_now_add=True)
    # album_art       = models.ImageField(upload_to="album_arts/", null=True, blank=True)
    album_art       = models.CharField(max_length=10000, null=True, blank=True)
    spotify         = models.CharField(max_length=500, null=True, blank=True)
    youtube         = models.CharField(max_length=500, null=True, blank=True)
    soundcloud      = models.CharField(max_length=500, null=True, blank=True)
    status          = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering    =   ['-released_on']
    
    class Meta:
        verbose_name_plural =   'songs'

    def __str__(self):
        return self.title + ' | ' + str(self.artist)

    def save(self, *args, **kwargs):
        if not self.id:
            self.album_art   =   self.compressImage(self.album_art)
        super(Song, self).save(*args, **kwargs)
    
    def compressImage(self,album_art):
        imageTemporary  =   Image.open(album_art)
        outputIOStream  =   BytesIO()
        imageTemporaryResized   =   imageTemporary.resize((1020,573))
        imageTemporary.save(outputIOStream, format='JPEG', quality=60)
        if imageTemporary.mode in ("RGBA", "P"):
            imageTemporary = imageTemporary.convert("JPEG")
        outputIOStream.seek(0)
        album_art   =   InMemoryUploadedFile(outputIOStream, 'ImageField', "%s.jpg" % album_art.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIOStream), None)
        return album_art

class Events(models.Model):
    title           = models.CharField(max_length=250, null=True)
    location        = models.CharField(max_length=250, null=True)
    entry_fee       = models.CharField(max_length=50, null=True)
    event_image     = models.ImageField(upload_to='events_images/', null=True, blank=True)
    purchase_link   = models.CharField(max_length=500, null=True, blank= True)
    created_on     = models.DateTimeField(auto_now_add=True, null=True)
    event_time      = models.TimeField(null=True)
    event_date      = models.DateField(null=True, blank=True)
    featured        = models.BooleanField(default=False, null=True)
    status          = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        verbose_name_plural =   'events'

    def __str__(self):
        return self.title 

    def save(self, *args, **kwargs):
        if not self.id:
            self.event_image   =   self.compressImage(self.event_image)
        super(Events, self).save(*args, **kwargs)
    
    def compressImage(self, event_image):
        imageTemporary          =   Image.open(event_image)
        outputIOStream          =   BytesIO()
        imageTemporaryResized   =   imageTemporary.resize((1020,573))
        imageTemporary.save(outputIOStream, format='JPEG', quality=60)
        outputIOStream.seek(0)
        event_image   =   InMemoryUploadedFile(outputIOStream, 'ImageField', "%s.jpg" % event_image.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIOStream), None)
        return event_image

class Team(models.Model):
    name = models.CharField(max_length=250, null=True)
    title = models.CharField(max_length=250, null=True)
    photo = models.ImageField(upload_to='Team_Passport_Photo/', null=True, blank=True)
    twitter = models.CharField(max_length=250, null=True, blank=True)
    facebook = models.CharField(max_length=250, null=True, blank=True)
    instagram = models.CharField(max_length=250, null=True, blank=True)
    youtube = models.CharField(max_length=250, null=True, blank=True)
    created_on     = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name + ' | ' + str(self.title)

    def save(self, *args, **kwargs):
        if not self.id:
            self.photo   =   self.compressImage(self.photo)
        super(Team, self).save(*args, **kwargs)
    
    def compressImage(self, photo):
        imageTemporary          =   Image.open(photo)
        outputIOStream          =   BytesIO()
        imageTemporaryResized   =   imageTemporary.resize((1020,573))
        imageTemporary.save(outputIOStream, format='JPEG', quality=60)
        outputIOStream.seek(0)
        photo   =   InMemoryUploadedFile(outputIOStream, 'ImageField', "%s.jpg" % photo.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIOStream), None)
        return photo