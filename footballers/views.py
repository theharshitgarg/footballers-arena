# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.core.paginator import Paginator
from .models import FootballPlayer
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required

class PlayersListView(generic.ListView):

    template_name = 'footballers/footballers_list.html'
    context_object_name = 'footballers_list'
    paginate_by = 10

    def get_queryset(self):
        """Return all the objects."""

        return FootballPlayer.objects.all()


def player_detail_view(request, pk):
    player = get_object_or_404(FootballPlayer, pk=pk)
    serialized_player = player.json_equivalent
    
    return render(request, 'footballers/footballer_details.html', 
    	{'footballer': player, 'serialized_player': serialized_player})