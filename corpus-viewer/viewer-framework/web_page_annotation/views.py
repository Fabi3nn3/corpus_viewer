from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from web_page_annotation.models import *
import random
import string
# Create your views here.

def index(request):
    #return HttpResponse("<h1>This is web_page_annotation</h1>")
	# Example_Model.objects.all().delete()
	if Annotation_Model.objects.count()==0:
		list_objects = []
		for index in range(0, 10000):
			list_objects.append(
				Annotation_Model(
                    hit="".join( [random.choice(string.digits) for i in range(3)] ),
                    task="".join( [random.choice(string.ascii_lowercase) for i in range(8)] ),
					rating_m="".join([random.choice(string.ascii_lowercase) for i in range(8)])
				)
			)

		Annotation_Model.objects.bulk_create(list_objects)

	return JsonResponse({})
