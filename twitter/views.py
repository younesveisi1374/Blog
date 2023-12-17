from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Message

# def messageView(request):
#    return render(request,'twitter/index.html',{'name': 'Younes'})


class MessageView(ListView):
    model = Message
    template_name = 'twitter/index.html'
    # def get(self, request):
    #    return render(request, 'twitter/index.html', {'name': 'Younes'})
