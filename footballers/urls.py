from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PlayersListView.as_view(), name='players'),
    # url(r'^$', views.PlayersListView.as_view(), name='player_detail'),
    url(r'^(?P<pk>[-\w]+)/$', views.player_detail_view, name='player-detail')
]
