from django.db import models


class Venue(models.Model):

    #unique properties
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=2)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.name, self.city, self.state, self.country)



class Show(models.Model):

    #show was @ a venue relationship
    venue = models.ForeignKey(Venue, on_delete=models.DO_NOTHING)

    #unique properties
    show_key = models.CharField(max_length=7)
    date = models.DateField()

    def __str__(self):
        return '{} - {}'.format(self.date, self.venue)



class Set(models.Model):

    #set took place @ show relationship
    show = models.ForeignKey(Show, on_delete=models.DO_NOTHING)

    #songs played during this set
    songs = models.ManyToManyField('Song', through='Performance')

    #unique properties
    name = models.CharField(max_length=64)

    def __str__(self):
        return '{}'.format(self.name)



class Song(models.Model):


    #unique properties
    name = models.CharField(max_length=128)
    cover = models.CharField(max_length=64)


    def __str__(self):
        return '{} - {}'.format(self.name, self.name)



class Performance(models.Model):

    #performance of a song relationship
    song = models.ForeignKey(Song, on_delete=models.DO_NOTHING)

    #performance took place during a set
    set = models.ForeignKey(Set, on_delete=models.DO_NOTHING)


    #unique properties
    track = models.IntegerField()
    segue = models.CharField(max_length=1)
    notes = models.CharField(max_length=128)
    guest = models.CharField(max_length=64)

    def __str__(self):
        return '{} - {}'.format(self.set.show.date, self.song.name)



