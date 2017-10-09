# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect, HttpResponse
from time import gmtime, strftime

# Create your views here.
def index (request) :
    return render(request, 'sessionWords/index.html')

def process (request) :
    if request.method == "POST":
        print request.POST
        val = {}
        arr = []

        if "words" not in request.session :
            arr = []
        else :
            arr = request.session["words"]

        val["word"] = request.POST["word"]
        if "color" in request.POST :
            val["color"] = request.POST["color"]
        if "bigFont" in request.POST :
            val["bigFont"] = 800        
        val["dateTime"] = strftime("%Y-%m-%d %H:%M %p", gmtime())
        arr.append(val)   
        request.session["words"] = arr
        
        print arr
    
        # request.session["dojoLocation"] = request.POST["dojoLocation"]
        # request.session["language"] = request.POST["language"]
        # request.session["comments"] = request.POST["comments"]
        # print request.session
    return redirect ('/session/result')

def result (request) :
     return render(request, 'sessionWords/result.html')

def clear (request) :
    print "in clear"
    request.session.flush()
    return redirect("/session")
    
    