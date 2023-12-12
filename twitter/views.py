from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# def messageView(request):
#    return render(request,'twitter/index.html',{'name': 'Younes'})


class MessageView(TemplateView):
    template_name = 'twitter/index.html'
    #def get(self, request):
    #    return render(request, 'twitter/index.html', {'name': 'Younes'})
