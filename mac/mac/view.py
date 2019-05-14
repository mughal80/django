from django.http import  HttpResponse
from django.shortcuts import render

def index(request):
    params = {'data': 'Home'}
    return render(request, 'index.html', params)
    # return HttpResponse('<h1>Home</h1>')

def about(request):
    params ={'data':'About'}
    return render(request, 'about.html',params)
    # return HttpResponse('<h1>About</h1>')