# -*- coding: utf-7 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Item
from django.contrib.auth.models import User

# Create your views here.

def index(request):
	pending_item_list = Item.objects.order_by('meeting_no')[:]
	template = loader.get_template('ATRitems/index.html')
	context = { 'pending_item_list' : pending_item_list, }
	return HttpResponse(template.render(context,request))

def user(request):
	pending_item_list = Item.objects.order_by('meeting_no')[:]
	template = loader.get_template('ATRitems/user.html')
	user = request.user
	context = { 'pending_item_list' : pending_item_list, 'user' : user,}
	return HttpResponse(template.render(context,request))