# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class FootballPlayer(models.Model):
	name = models.CharField(max_length=25)
	nationality = models.CharField(max_length=19)
	national_position = models.CharField(max_length=3)
	national_kit = models.CharField(max_length=2)
	club = models.CharField(max_length=17)
	club_position = models.CharField(max_length=3)
	club_kit = models.CharField(max_length=2)
	club_joining = models.CharField(max_length=10)
	contract_expiry = models.CharField(max_length=4)
	rating = models.IntegerField()
	height = models.CharField(max_length=6)
	weight = models.CharField(max_length=5)
	preffered_foot = models.CharField(max_length=5)
	birth_date = models.CharField(max_length=10)
	age = models.IntegerField()
	preffered_position = models.CharField(max_length=9)
	work_rate = models.CharField(max_length=15)
	weak_foot = models.IntegerField()
	skill_moves = models.IntegerField()
	ball_control = models.IntegerField()
	dribbling = models.IntegerField()
	marking = models.IntegerField()
	sliding_tackle = models.IntegerField()
	standing_tackle = models.IntegerField()
	aggression = models.IntegerField()
	reactions = models.IntegerField()
	attacking_position = models.IntegerField()
	interceptions = models.IntegerField()
	vision = models.IntegerField()
	composure = models.IntegerField()
	crossing = models.IntegerField()
	short_pass = models.IntegerField()
	long_pass = models.IntegerField()
	acceleration = models.IntegerField()
	speed = models.IntegerField()
	stamina = models.IntegerField()
	strength = models.IntegerField()
	balance = models.IntegerField()
	agility = models.IntegerField()
	jumping = models.IntegerField()
	heading = models.IntegerField()
	shot_power = models.IntegerField()
	finishing = models.IntegerField()
	long_shots = models.IntegerField()
	curve = models.IntegerField()
	freekick_accuracy = models.IntegerField()
	penalties = models.IntegerField()
	volleys = models.IntegerField()
	gk_positioning = models.IntegerField()
	gk_diving = models.IntegerField()
	gk_kicking = models.IntegerField()
	gk_handling = models.IntegerField()
	gk_reflexes = models.IntegerField()

	def __str__(self):
		return self.name+' '+self.club

	@property
	def json_equivalent(self):
		dictionary = {}
		for field in self._meta.fields:
			dictionary[field.name] = self.__getattribute__(field.name)
		return dictionary
