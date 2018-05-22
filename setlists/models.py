from django.db import models


class Venue(models.Model):

    #unique properties
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=2)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.name, self.city, self.state, self.country)


#Show filters models manager for custom queries

class ShowFilters(models.Manager):

    #return all shows by specific year
    def by_year(self, year):

        return self.filter(date__year=year).all().order_by('date').reverse()

    #returns unique years
    def years_list(self):

        return self.dates('date', 'year', order='DESC')


class Show(models.Model):

    #show was @ a venue relationship
    venue = models.ForeignKey(Venue, on_delete=models.DO_NOTHING)

    #unique properties
    show_key = models.CharField(max_length=7)
    date = models.DateField()

    filters = ShowFilters()

    def __str__(self):
        return '{} - {}'.format(self.date, self.venue)



class Set(models.Model):


    #songs played during this set
    songs = models.ManyToManyField('Song', through='Performance')

    #unique properties
    name = models.CharField(max_length=64)

    def __str__(self):
        return '{}'.format(self.name)


class Song(models.Model):

    #unique properties
    name = models.CharField(max_length=128)
    cover = models.CharField(max_length=64, null=True)

    def __str__(self):
        return '{}'.format(self.name)

class PerformanceStats(models.Manager):

    #build function to get times played
    def times_played(self):
        pass

class Performance(models.Model):

    #performance of a song relationship
    song = models.ForeignKey(Song, on_delete=models.DO_NOTHING)

    #performance took place at a show
    set = models.ForeignKey(Set, on_delete=models.DO_NOTHING)

    show = models.ForeignKey(Show, on_delete=models.DO_NOTHING)

    #unique properties
    track = models.IntegerField()
    segue = models.CharField(max_length=1, null=True)
    notes = models.CharField(max_length=128, null=True)
    guest = models.CharField(max_length=64, null=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.show.date, self.set.name, self.song.name)



