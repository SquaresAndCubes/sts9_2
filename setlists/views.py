from django.http import HttpResponse
from django.template import loader
from .models import Venue, Show

# Create your views here.


def test(request):

    setlists = Show.objects.all()

    template = loader.get_template('setlists/test.html')
    context = {
        'setlists': setlists,
    }
    return HttpResponse(template.render(context, request))

def setlists(request):

    setlists = Show.objects.all()

    template = loader.get_template('setlists/index.html')

    context = {
        'setlists': setlists,
    }
    return HttpResponse(template.render(context, request))


def songs(request):

    songs = Song.objects.all()

    template = loader.get_template('songs/index.html')

    context = {
        'songs': songs,
    }
    return HttpResponse(template.render(context, request))