from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# def messageView(request):
#    return render(request,'twitter/index.html',{'name': 'Younes'})


class MessageView(View):
    def get(self, request):
        return render(request, 'twitter/index.html', {'name': 'Younes'})
