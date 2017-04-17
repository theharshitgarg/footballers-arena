# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator
from .models import FootballPlayer


class PlayersListView(generic.ListView):

    template_name = 'footballers/footballers_list.html'
    context_object_name = 'footballers_list'
    paginate_by = 10

    def get_queryset(self):
        """Return all the objects."""
        return FootballPlayer.objects.all()
