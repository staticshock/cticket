from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'cticket.views.index', name='home'),
    url(r'^traffic-stops/', 'cticket.views.traffic_stops'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
