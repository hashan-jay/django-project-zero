from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page_view(request):
    return HttpResponse("<h1>Hello, World!<h1><p>Welcome to my custom Django homepage.</p><h2>This is HashJay</h2>")

