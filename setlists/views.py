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

    #grabs most recent year object and pulls year
    latest_year = years_list[0].year

    #if no year is given in url sets year to most recent
    if year == None:
        year = latest_year

    setlists = Show.filter.by_year(year)

    #counts num of shows in the year
    show_count = setlists.count()

    template = loader.get_template('setlists/index.html')

    context = {
        'setlists': setlists,
        'year': year,
        'show_count': show_count,
        'years_list': years_list,
    }
    return HttpResponse(template.render(context, request))


def songs(request):

    songs = Song.filter.all_songs()

    template = loader.get_template('songs/index.html')

    context = {
        'songs': songs,
    }
    return HttpResponse(template.render(context, request))

def song(request, song):

    #gets song object and finds all shows it was played at
    shows = Song.filter.one_song(song).all_shows_played().order_by('set__show__date').reverse()

    template = loader.get_template('songs/song.html')

    context = {
        'song': song,
        'shows': shows,
    }
    return HttpResponse(template.render(context, request))