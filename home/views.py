# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
from django.http import JsonResponse
import logging

from django.http import Http404

# Get an instance of a logger
logger = logging.getLogger('kl')


response_data = {}
response_data['result'] = 'SUCCESS'
response_data['message'] = 'OK'


# Create your views here.

def index(request):
	  context = {'ecommerce':''}
   	return render(request, 'ecommerce/index.html', context)

def sigup(request):

	  context = {'ecommerce':''}
   	return render(request, 'ecommerce/sigup.html', context)

@csrf_exempt
def update(request):
	  context = {'questions': ""}
   	return render(request, 'home/update.html', context)
