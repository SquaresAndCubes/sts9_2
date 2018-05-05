from django.http import HttpResponse
from django.template import loader
from .models import Venue, Show

# Create your views here.


def test(request):

    venue_list = Venue.objects.all()
    show_list = Show.objects.all()
    venue_cnt = Venue.objects.all().count()
    show_cnt = Show.objects.all().count()

    template = loader.get_template('setlists/test.html')
    context = {
        'venue_list': venue_list,
        'show_cnt': show_cnt,
        'venue_cnt': venue_cnt,
        'show_list': show_list,
    }
    return HttpResponse(template.render(context, request))