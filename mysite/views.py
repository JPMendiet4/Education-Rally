from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'mysite/index.html')
