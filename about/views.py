from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("This would be the about page")