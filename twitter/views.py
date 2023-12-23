from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from .models import Post
from django.contrib.auth import logout
from .forms import PostForm
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.core.paginator import Paginator


def logout_view(request):
    logout(request)

    # Redirect to a success page.
# def messageView(request):
#    return render(request,'twitter/index.html',{'name': 'Younes'})


class HomeView(ListView):
    # model = Post
    template_name = 'twitter/index.html'
    # def get(self, request):
    #    return render(request, 'twitter/index.html', {'name': 'Younes'})
    paginate_by = 1

    def get(self, request):
        posts = Post.objects.all()
        paginator = Paginator(posts, self.paginate_by)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'post_list': page_obj
        }
        return render(request, self.template_name, context)


class NewPostView(CreateView):
    model = Post
    template_name = 'twitter/post_new.html'
    form_class = PostForm
    success_url = reverse_lazy('home')
    # fields = ['title','excerpt','body','author','date','photo']


class PostDetailView(DetailView):
    model = Post
    template_name = 'twitter/post_single.html'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'twitter/post_update.html'
    fields = ['title', 'excerpt', 'body', 'photo']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'twitter/post_delete.html'
    success_url = reverse_lazy('home')
