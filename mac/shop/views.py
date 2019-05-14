from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    params={'data': 'shopIndex'}
    return render( request, 'shop/index.html', params)
    # return HttpResponse("Index Shop")
def about(request):
    params={'data': 'shopabout'}
    return render( request,'shop/about.html', params)   
def contact(request):   
    return HttpResponse("Shop Contact us")
def search(request):   
    return HttpResponse("Shop search us")
def prodview(request):   
    return HttpResponse("Shop prodview us")
def checkout(request):   
    return HttpResponse("Shop checkout us")
def tracker(request):   
    return HttpResponse("Shop tracker us")
