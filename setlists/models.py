from django.db import models
from django.db.models import Count, Min, Max, Window, DateTimeField
from django.utils.text import slugify
from django.db.models import OuterRef, Subquery, DateField
from django.db.models.functions.window import Rank, DenseRank, RowNumber, NthValue
from django.db.models.functions import TruncDate



class Venue(models.Model):

    #unique properties
    name = models.CharField(max_length=64, null=False)
    city = models.CharField(max_length=64, null=False)
    state = models.CharField(max_length=4, null=True)
    country = models.CharField(max_length=4, null=False)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.name, self.city, self.state, self.country)


class ShowFilters(models.Manager):

    def by_year(self, year):
        # return only shows of the specified year
        return self.filter(date__year=year).order_by('date').reverse()

    def years_list(self):
        # get list of unique years
        return self.dates('date', 'year', order='DESC')

    def show(self, show_id):
        # return one show
        return self.get(id=show_id)

    def song_occurances(self, song_id):

        #create list for filtered queryset
        shows_list = []

        #for loop through all shows and append shows with matching song_ids to shows_list
        for show in self.annotate(rank=Window(order_by=TruncDate('date').desc(), expression=Rank())):

            if song_id in show.set_set.values_list('performance__song_id', flat=True):

                shows_list.append(show)

        return shows_list



class Show(models.Model):

    #show was @ a venue relationship
    venue = models.ForeignKey(Venue, null=True, on_delete=models.SET_NULL)

    #remove after data import
    show_key = models.CharField(max_length=7, null=True)

    #unique properties
    date = models.DateField()

    #custom model manager sticky
    filter = ShowFilters()

    #default model manager
    objects = models.Manager()

    ##########ADD SLUGFIELD#############

    #slug = models.SlugField()

    #function for getting sets ordered by set position
    def get_sets(self):

        return self.set_set.order_by('set_pos')

    def __str__(self):
        return '{} - {}'.format(self.date, self.venue)


class Set(models.Model):

    #SET choices to reduce entry errors

    SET1 = 'S1'
    SET2 = 'S2'
    SET3 = 'S3'
    ENCORE = 'E1'
    ENCORE2 = 'E2'
    AXE = 'AX'
    PA = 'PA'

    SET_CHOICES = (
        (SET1, 'Set 1'),
        (SET2, 'Set 2'),
        (SET3, 'Set 3'),
        (ENCORE, 'Encore'),
        (ENCORE2, 'Encore 2'),
        (AXE, 'Axe The Cables'),
        (PA, 'PA Set')
    )

    # unique properties
    name = models.CharField(
        max_length=2,
        choices=SET_CHOICES,
        default=SET1,
        null=False,
    )

    #set took place @ show relationship
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    #songs played during this set
    songs = models.ManyToManyField('Song', through='Performance')

    #set position in show
    set_pos = models.IntegerField()

    #get performances
    def get_songs(self):

        return self.performance_set.order_by('track')

    def __str__(self):
        return '{} - {} \n{}\n'.format(self.show, self.name, self.performance_set.values_list('song__name'))


class SongsLists(models.Manager):

    def all_songs_play_count(self):
        #returns all songs ordered by play count
        return self.annotate(play_count=Count('performance__set__show_id', distinct = True),
                             #gets the date song was first played
                             first_played=Min('performance__set__show__date'),
                             #gets most recent date played
                             last_played=Max('performance__set__show__date'),
                             ).order_by('play_count').reverse()

    def song(self, song_id):
        #returns song name and all shows played ordered by date
        return self.get(id=song_id).name, self.get(id=song_id).set_set.distinct('show__date').order_by('show__date').reverse()


class Song(models.Model):

    #unique properties
    name = models.CharField(max_length=128, null=False)
    artist = models.CharField(max_length=64, null=False)

    #model manager sticky
    data = SongsLists()

    #default models manager
    objects = models.Manager()

    def __str__(self):
        return '{} - {}'.format(self.name, self.artist)


class PerformanceStats(models.Manager):
    pass


class Performance(models.Model):

    #performance of a song relationship
    song = models.ForeignKey(Song, null=True, on_delete=models.SET_NULL)

    #performance took place during a set
    set = models.ForeignKey(Set, on_delete=models.CASCADE)

    #unique properties
    track = models.IntegerField()
    segue = models.CharField(max_length=2, null=True)
    notes = models.CharField(max_length=128, null=True)
    guest = models.CharField(max_length=64, null=True)

    #custom model manager sticky
    stats = PerformanceStats()

    #default model manager
    objects = models.Manager()

    def __str__(self):
        return '{} - {}'.format(self.set.show.date, self.song.name)



