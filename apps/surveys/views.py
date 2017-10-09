# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect, HttpResponse

# Create your views here.
def index (request) :
    return render(request, 'surveys/survey.html')

def process (request) :
    if request.method == "POST":
        print request.session
        if "attempts" not in request.session :
            request.session["attempts"] = 0
            
        request.session["attempts"] = request.session["attempts"] + 1
        request.session["name"] = request.POST["name"]
        request.session["dojoLocation"] = request.POST["dojoLocation"]
        request.session["language"] = request.POST["language"]
        request.session["comments"] = request.POST["comments"]
        print request.session
    return redirect ('/result')

def result (request) :
    return render(request, 'surveys/surveyResult.html')
    
    