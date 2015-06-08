from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Examples:
    url(r'^$', 'cticket.views.index', name='home'),
    url(r'^traffic-stops/', 'cticket.views.traffic_stops'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
] + staticfiles_urlpatterns()
