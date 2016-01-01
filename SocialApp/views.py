from django.shortcuts import render
from models import Test
# Create your views here.

def index(request):
    t = Test()
    t.last_name="Ana"
    t.first_name="Maria"
    context ={
        'test': t
    }
    return render(request,'index.html',context)