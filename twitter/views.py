from django.http import HttpResponse
from django.shortcuts import render

def messageView(request):
    return render(request,'twitter/index.html',{'name': 'Younes'})