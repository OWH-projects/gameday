from django.conf.urls import *

urlpatterns = patterns('gameday.views',
    (r'^/(?P<season>[0-9]+)/(?P<team>[a-zA-Z0-9_.-]+)$', 'Opponent'),
    (r'^', 'Main'),
)
