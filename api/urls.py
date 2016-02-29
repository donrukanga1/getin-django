from django.conf.urls import patterns, include, url

from api.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'getin.views.home', name='home'),
    # url(r'^api/', include('api.urls')),
    url(r'^login/', Login.as_view()),
    url(r'^search/$', Search.as_view(), name="search"),

    url(r'^girls/register/', RegisterPregnantGirl.as_view(), name='register-pregnant-girl'),
    url(r'^girls/list/', ListPregnantGirls.as_view(), name='list-pregnant-girls'),

    url(r'^appointments/upcoming/', UpcomingAppointments.as_view(), name='upcoming-appointments'),
    url(r'^appointments/missed/', MissedAppointments.as_view(), name='missed-appointment'),

    url(r'^vhts/list/', VHTList.as_view(), name='vht-list'),

)
