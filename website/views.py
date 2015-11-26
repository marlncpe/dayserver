# -*- encoding: utf-8 -*-

from rest_framework.generics import RetrieveAPIView
from rest_framework import serializers
from django.contrib.auth.models import User
from django.shortcuts import render
from website.models import *
from serializers import *
from rest_framework import viewsets, generics, filters

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User

class LoginView(RetrieveAPIView):
	serializer_class = UserSerializer
	model = User
	queryset = User.objects.all()
	
	
	def get_object(self):
		return self.request.user