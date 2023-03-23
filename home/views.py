from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request): 
    # response = HttpResponse()
    return render(request, 'page/home.html')
def index2(request): 
    # response = HttpResponse()
    return render(request, 'page/tintuc.html')
def index3(request):
    return render(request, 'page/contact.html')