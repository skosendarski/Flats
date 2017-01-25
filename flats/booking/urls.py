from django.conf.urls import url
from . import views


app_name = 'booking'
urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^(?P<pk>[0-9]+)/$', views.SelectView.as_view(), name='select'),
    url(r'^(?P<pk>[0-9]+)/booked$', views.booked_view, name='booked'),
    url(r'^search/$', views.search_view, name='search'),

]
