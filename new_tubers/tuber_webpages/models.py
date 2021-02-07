from django.db import models
from ckeditor.fields import RichTextField


class Services(models.Model):
    img = models.ImageField(upload_to='media/service/%Y/')
    title = models.CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    emial = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    flink = models.CharField(max_length=100)
    ilink = models.CharField(max_length=100)
    tlink = models.CharField(max_length=100)
    ylink = models.CharField(max_length=100)

    def __str__(self):
        return self.emial


class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    lin_link = models.CharField(max_length=255)
    yt_link = models.CharField(max_length=255, default=0)
    photo = models.ImageField(upload_to='media/team/%Y/%m/%d')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider/%Y/')
    tuber_link = models.CharField(max_length=255, default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline

