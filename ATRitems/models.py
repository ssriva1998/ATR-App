# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
	year_no = models.CharField(max_length=200)
	meeting_no = models.CharField(max_length=200)
	agenda_no = models.IntegerField()
	agenda_item = models.TextField()
	decision_taken = models.TextField()
	functionary = models.ManyToManyField(User)
	status = models.TextField()
	is_complete = models.BooleanField(default = False)		

	def __str__(self):
		return self.year_no + "/" + self.meeting_no + "/" + str(self.agenda_no)
	

