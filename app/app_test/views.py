from django.shortcuts import render, get_object_or_404
from .models import ChaiVarity

# Create your views here.

def app_2_home(request):
    return render(request, ("app_test/index.html"))

def chai(request):

    chais = ChaiVarity.objects.all()

    return render(request,"app_test/chai.html", {'chais':chais})

def chai_details(request, chai_id):

    chai = get_object_or_404(ChaiVarity, pk=chai_id)

    return render(request, 'app_test/chai_details.html', {'chai':chai})