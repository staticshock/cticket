from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def traffic_stops(request):
    template = loader.get_template('traffic_stops.html')
    # TODO search db for request.GET["badge_num"], attach results to context:
    return HttpResponse(template.render())
