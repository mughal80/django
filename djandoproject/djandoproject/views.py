
from django.http import  HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name': "Adeeb", 'email': "m.adeebmughal@gmail.com"}
    return  render(request, 'index.html', params)
    # return HttpResponse("Hello")
def about(request):
    textVal =request.GET.get('text')
    text=""
    for char in textVal:
        if char not in '0123456789':
            text += char
    print(text.__len__())

    params ={'djtext': text}
    # print(textVal)
    # return HttpResponse("<h1>"+textVal+"</h1>")
    return render(request, 'anylizer.html', params)