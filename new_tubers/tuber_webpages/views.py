from django.shortcuts import render
from .models import Slider, Team, ContactInfo, Services
from youtubers.models import Youtuber


def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_youtubers = Youtuber.objects.order_by('-created_date')
    contact_info = ContactInfo.objects.all()
    data = {
        'sliders': sliders,
        'teams': teams,
        'featured_youtubers': featured_youtubers,
        'all_youtubers': all_youtubers,
        'contact_info': contact_info
    }
    return render(request, 'tuber_webpages/home.html', data)


def about(request):
    teams = Team.objects.all()
    service = Services.objects.all()
    contact_info = ContactInfo.objects.all()
    data = {
        'teams': teams,
        'service': service,
        'contact_info': contact_info
    }
    return render(request, 'tuber_webpages/about.html', data)


def services(request):
    service = Services.objects.all()
    contact_info = ContactInfo.objects.all()
    data = {
        'service': service,
        'contact_info': contact_info
    }
    return render(request, 'tuber_webpages/services.html', data)


def contact(request):
    contact_info = ContactInfo.objects.all()
    data = {
    'contact_info': contact_info
    }
    return render(request, 'tuber_webpages/contact.html', data)

