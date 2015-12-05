from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from experience.models import Experience
import datetime, datetime
from django.utils import timezone

def experience_index(request):
	experience = Experience.objects.all()
	return render(request, 'experience/index.html', {'experience' : experience})

def testy(request):
	return render(request, 'experience/two.html')
