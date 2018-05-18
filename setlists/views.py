from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.


def home():
    pass

def stats():
    pass


def test(request):

    setlists = Show.objects.all()

    template = loader.get_template('setlists/test.html')
    context = {
        'setlists': setlists,
    }
    return HttpResponse(template.render(context, request))

def year(request, year=None):

    years_list = Show.filter.years_list()

    setlists = Show.filter.by_year(year)

    show_count = len(setlists)

    template = loader.get_template('setlists/index.html')

    context = {
        'setlists': setlists,
        'year': year,
        'show_count': show_count,
    }
    return HttpResponse(template.render(context, request))


def songs(request):

    songs = Song.objects.all()

    template = loader.get_template('songs/index.html')

    context = {
        'songs': songs,
    }
    return HttpResponse(template.render(context, request))