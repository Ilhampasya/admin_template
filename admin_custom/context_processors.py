from django.conf import settings
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.text import capfirst

site = admin.site

def applist(request):
    from django.conf import settings
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.text import capfirst

site = admin.site

def applist(request):
	return {'app_lists': site.get_app_list(request)}