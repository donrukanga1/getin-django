from django.conf.urls import patterns, url

from views import GirlsList, GirlsMap, UpdateGirl, DeleteGirl

urlpatterns = patterns(
    '',
    # url(r'^$', AdminDashboard.as_view(), name='dashboard-admin'),
    url(r'^girls/list/$', GirlsList.as_view(), name='girls-list'),
    url(r'^girls/map/$', GirlsMap.as_view(), name='girls-map'),
    url(r'^girls/(?P<pk>[0-9]+)/edit$', UpdateGirl.as_view(), name='dashboard-admin-girls-edit'),
    url(r'^girls/(?P<pk>[0-9]+)/delete', DeleteGirl.as_view(), name='dashboard-admin-girls-delete'),


)

