# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import Item

# Register your models here.
# user.partner_set.filter(slug=requested_slug).exists():
class ItemModelAdmin(VersionAdmin):
    class Meta:
    	model = Item
    list_display = ('agenda_item',  )
    def get_fields(self, request, obj=None):
        if not request.user.is_superuser:
            self.fields = ('is_complete', 'functionary', 'status', )  
        else: 
            self.fields = ('year_no','meeting_no', 'agenda_no', 'agenda_item', 'decision_taken', 'is_complete', 'functionary', 'status', )
        return self.fields
    def get_queryset(self, request):
        qs = super(ItemModelAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(functionary = request.user)
        return qs
    def has_add_permission(self, request):
    	if request.user.is_superuser:
    		return True
    	return False 
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj is not None and not (obj in request.user.item_set.all()):
            return False
    	return True
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
admin.site.register(Item, ItemModelAdmin)
