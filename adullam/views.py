from django.shortcuts import render
from .models import Sites, Graphic, Defaultpic

# Create your views here.


def index(request):
    sites = Sites.objects.all()
    images = Graphic.objects.all()
    img = Defaultpic.objects.all()
    context = {
        'sites':sites,
        'images':images,
        'img': img,
    }
    return render(request, 'adullam/index.html', context)


def about(request):
    img = Defaultpic.objects.all()
    context = {
        'img':img
    }
    return render(request, 'adullam/about.html', context)


def contact(request):
    return render(request, 'adullam/contact.html')


def sites(request):
    sites = Sites.objects.all()
    context = {
        'sites':sites
    }
    return render(request, 'adullam/sites.html', context)