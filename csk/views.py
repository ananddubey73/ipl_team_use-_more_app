from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def msd(request):
    return render(request,'dhoni.html')


def raina(request):
    return HttpResponse('Raina was good allrounder in india team')


