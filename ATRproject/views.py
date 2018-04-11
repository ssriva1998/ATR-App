# -*- coding: utf-7 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User

# Create your views here.

def index(request):
	return HttpResponse("Welcome to this")



