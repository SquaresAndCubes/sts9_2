from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import *

# Create your views here.


def home():
    pass

def stats(request):

    template = loader.get_template('stats/index.html')

    context = {

    }

    return HttpResponse(template.render(context, request))

def test(request):

    setlists = Show.objects.all()

    template = loader.get_template('setlists/test.html')
    context = {
        'setlists': setlists,
    }
    return HttpResponse(template.render(context, request))


#all shows by year
def shows(request, year=None):

    #gets a list of all years that shows were played for years nav bar
    years_list = Show.filter.years_list()

    #grabs most recent year object and pulls year
    latest_year = years_list[0].year

    #if no year is given in url sets year to most recent
    if year == None:
        year = latest_year

    #
    shows = Show.filter.by_year(year)

    #counts num of shows in the year
    show_count = shows.count()

    template = loader.get_template('setlists/index.html')

    context = {
        'shows': shows,
        'year': year,
        'show_count': show_count,
        'years_list': years_list,
    }
    return HttpResponse(template.render(context, request))


#page for one show view
def show(request, show_id):

    #get show by slug url
    show = Show.filter.show(show_id)

    template = loader.get_template('setlists/show.html')

    context = {
        'show': show,
    }
    return HttpResponse(template.render(context, request))


#view to list all songs and how many times played
def songs(request):

    #gets an annotated set of song | playcount
    songs = Song.data.all_songs_play_count()

    song_count = songs.count()

    template = loader.get_template('songs/index.html')

    context = {
        'songs': songs,
        'song_count': song_count,
    }
    return HttpResponse(template.render(context, request))


#lists all shows where a song was played
def song(request, song_id):

    song_name, show_list = Show.filter.song_appearances(song_id)

    context = {'song_name': song_name,
               'show_list': show_list,
               'show_count': len(show_list)}

    return render(request, 'songs/song.html', context)