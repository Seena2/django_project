from django.shortcuts import render
from django.http import HttpResponse

# Views
def home(request):
    return HttpResponse ("<h1>Blogs Home</h1>")

def about(request):
    return HttpResponse ("<h1>Blogs About Page</h1>")
