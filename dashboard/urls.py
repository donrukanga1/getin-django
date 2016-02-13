from django.conf.urls import patterns, url

from views import GirlsList, GirlsMap, UpdateGirl, DeleteGirl, PresetMessagesList, BlastSmsView

urlpatterns = patterns(
    '',
    url(r'^$', GirlsList.as_view(), name='dashboard-admin'),
    url(r'^girls/list/$', GirlsList.as_view(), name='girls-list'),
    url(r'^girls/map/$', GirlsMap.as_view(), name='girls-map'),
    url(r'^girls/(?P<pk>[0-9]+)/edit$', UpdateGirl.as_view(), name='girls-edit'),
    url(r'^girls/(?P<pk>[0-9]+)/delete', DeleteGirl.as_view(), name='girls-delete'),

    url(r'^messages/$', PresetMessagesList.as_view(), name='messages'),
    url(r'^messages/blast/$', BlastSmsView.as_view(), name='blast-sms'),

)

