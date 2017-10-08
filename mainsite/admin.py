
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	"""docstring for PostAdmin"""
	list_display = ('title','slug','pub_date')


admin.site.register(Post,PostAdmin)