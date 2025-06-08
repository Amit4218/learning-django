from django.shortcuts import render

# Create your views here.

def app_2_home(request):
    return render(request, ("app_test/index.html"))