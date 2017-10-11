# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Post(models.Model):

	title = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField(default = timezone.now)
	auth = models.CharField(max_length=100,default = 'warlock921')


	class Meta:
		ordering = ('-pub_date',)

	def __str__(self):
		return self.title