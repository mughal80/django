from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    params={'data': 'blogIndex'}
    return render( request, 'blog/index.html', params)
    # return HttpResponse("Index Blog")
def about(request):
    params={'data': 'shopIndex'}
    return render( request, 'blog/about.html', params)
    # return HttpResponse("About Blog")