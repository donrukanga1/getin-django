from django.conf.urls import patterns, include, url

from api.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'getin.views.home', name='home'),
    # url(r'^api/', include('api.urls')),
    url(r'^girls/register/', RegisterPregnantGirl.as_view(), name='register-pregnant-girl'),
    url(r'^girls/list/', ListPregnantGirls.as_view(), name='list-pregnant-girls'),


)
