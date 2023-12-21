from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView,ListView, CreateView,DetailView
from .models import Post
from django.contrib.auth import logout
from .forms import PostForm
from django.urls import reverse_lazy


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


class NewPostView(CreateView):
    model = Post
    template_name = 'twitter/post_new.html'
    form_class = PostForm
    success_url = reverse_lazy('home')
    # fields = ['title','excerpt','body','author','date','photo']


class PostDetailView(DetailView):
    model = Post
    template_name = 'twitter/post_single.html'