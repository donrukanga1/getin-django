from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'getin.views.home', name='home'),
    url(r'^api/', include('api.urls')),

    url(r'^dashboard/', include('dashboard.urls')),

    # Authentication
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name="login"),
    url(r'^accounts/login/', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),

    url(r'^admin/', include(admin.site.urls)),
)
