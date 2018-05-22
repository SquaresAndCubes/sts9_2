import csv
import os
import datetime
from django.conf import settings
from setlists import models



def import_venues():
    data_filepath = "shows.csv"
    results = {"created": 0, "skipped": 0}
    with open(data_filepath, "r") as f:
        reader = csv.reader(f)
        # skip header
        next(reader, None)
        for row in reader:

            # get_or_create returns 2 things, the first thing is the object we wanted, and the second thing
            # is a true / false value that lets us know if the object was newly created or if was already there
            new_obj, created = models.Venue.objects.get_or_create(name=row[2], city=row[3], state=row[4],
                                                                  country=row[5])

            # this is just being done for our print statement at the end, to let us know how many things were imported
            if created:
                results["created"] += 1
            else:
                results["skipped"] += 1

    print("Finished - Created {} Venues, Duplicates: {}".format(results["created"], results["skipped"]))




def import_shows():
    # path to our csv file
    data_filepath = "shows.csv"
    results = {"created": 0, "skipped": 0}
    with open(data_filepath, "r") as f:
        reader = csv.reader(f)
        # skip header
        next(reader, None)
        for row in reader:
            # by asking for a venue by the name, city, state and country, we ensure that we are getting the correct venue
            venue = models.Venue.objects.get(name=row[2], city=row[3], state=row[4], country=row[5])

            show_date = datetime.datetime.strptime(row[1], '%Y-%m-%d')

            # the new show needs to be saved after we create it
            new_show = models.Show(show_key=row[0], date=show_date, venue=venue)

            # thats done here
            new_show.save()

            # done for our print statement at the end
            results["created"] += 1
    print("Finished - Created {} Shows".format(results["created"]))


def import_sets():
    data_filepath = 'songs.csv'
    results = {"created": 0, "skipped": 0}
    with open(data_filepath, "r") as f:
        reader = csv.reader(f)
        # skip header
        next(reader, None)
        for row in reader:



            new_set, created = models.Set.objects.get_or_create(name=row[3])

            if created:
                results["created"] += 1
            else:
                results["skipped"] += 1

        print("Finished - Created {} Sets, Duplicates: {}".format(results["created"], results["skipped"]))

def import_songs():
    data_filepath = 'songs.csv'
    results = {"created": 0, "skipped": 0}
    with open(data_filepath, "r") as f:
        reader = csv.reader(f)
        # skip header
        next(reader, None)
        for row in reader:

            new_song, created = models.Song.objects.get_or_create(name=row[2], cover=row[7])

            if created:
                results['created'] += 1
            else:
                results['skipped'] += 1

        print("Finished - Created {} Songs, Duplicates: {}".format(results["created"], results["skipped"]))

def import_performances():
    data_filepath = 'songs.csv'
    results = {"created": 0, "skipped": 0}
    with open(data_filepath, "r") as f:
        reader = csv.reader(f)
        # skip header
        next(reader, None)
        for row in reader:

            song = models.Song.objects.get(name=row[2])

            set = models.Set.objects.get(name=row[3])

            show = models.Show.filters.get(show_key=row[1])

            new_perf = models.Performance(song=song, set=set, show=show, track=row[4], segue=row[5], notes=row[6], guest=row[8])

            new_perf.save()

            results["created"] += 1
    print("Finished - Created {} Performances".format(results["created"]))

