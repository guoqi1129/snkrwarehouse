from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return render(request,'login.html')
def test(request):
    print('11')
    return 0