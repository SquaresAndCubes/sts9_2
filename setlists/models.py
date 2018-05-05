from django.db import models


# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=2)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.name, self.city, self.state, self.country)



class Show(models.Model):
    show_key = models.CharField(max_length=7)
    date = models.DateField()
    venue = models.ForeignKey(Venue, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.date, self.venue.name, self.venue.city, self.venue.state, self.venue.country)


# class Set(models.Model):
#     show = models.ForeignKey(Show, on_delete=models.DO_NOTHING)
#     name = models.CharField(max_length=64)
#     position = models.IntegerField()
#
#
# class Song(models.Model):
#     name = models.CharField(max_length=128)
#     track = models.IntegerField()
#     set = models.ForeignKey(Set, on_delete=models.DO_NOTHING)
#     segue = models.BooleanField()
#     notes = models.CharField(max_length=128)
#     cover = models.CharField(max_length=64)
#     guest = models.CharField(max_length=64)