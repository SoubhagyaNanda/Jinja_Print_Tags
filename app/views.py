from django.shortcuts import render

# Create your views here.

def data_render(request):
    d={'name':'RAM','age':3}
    return render(request,'data_render.html',context=d)

def cond(request):
    d={'A':10,'B':50, 'C':30}
    return render(request,'cond.html',context=d)