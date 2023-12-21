from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Post
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    
    # Redirect to a success page.
# def messageView(request):
#    return render(request,'twitter/index.html',{'name': 'Younes'})


class HomeView(ListView):
    model = Post
    template_name = 'twitter/index.html'
    # def get(self, request):
    #    return render(request, 'twitter/index.html', {'name': 'Younes'})
