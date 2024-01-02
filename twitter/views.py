from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView, View, FormView
from .models import Post
from django.contrib.auth import logout
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import UpdateView, DeleteView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin


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


class NewPostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'twitter/post_new.html'
    form_class = PostForm
    success_url = reverse_lazy('home')
    # fields = ['title','excerpt','body','author','date','photo']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentGet(DeleteView):
    model = Post
    template_name = 'twitter/post_single.html'

    def get_context_data(self, **kwargs):
        # Call the parent class's `get_context_data` method to retrieve the existing context.
        # `super()` allows us to call methods of the base class in derived classes.
        context = super().get_context_data(**kwargs)

        # Add a new entry to the context dictionary with the key 'form'.
        # The value associated with 'form' is an instance of CommentForm.
        # CommentForm is likely a form class that handles user comments.
        context["form"] = CommentForm()

        # Return the updated context dictionary.
        # This context dictionary now includes all the data from the parent class,
        # as well as the new 'form' data we added for the CommentForm.
        return context


# Define a class named CommentPost which inherits from SingleObjectMixin and FormView.
class CommentPost(SingleObjectMixin, FormView):
    # Set the model that this view will operate on to 'Post'.
    model = Post
    
    # Set the form_class attribute to 'CommentForm', specifying what form to use.
    form_class = CommentForm
    
    # Define the template file that will be used when rendering the view.
    template_name = 'twitter/post_single.html'

    # Override the 'post' method to handle HTTP POST requests.
    def post(self, request, *args, **kwargs):
        # Retrieve the object related to this view.
        # In this context, it's likely to be the Post instance that is being commented on.
        self.object = self.get_object()
        
        # Call the parent class's 'post' method with all arguments to continue handling the POST request.
        return super().post(request, *args, **kwargs)

    # Override the 'form_valid' method which is called when valid form data has been POSTed.
    def form_valid(self, form):
        # Create a new tweet object from the form but don't save it to the database yet (commit=False).
        tweet = form.save(commit=False)
        
        # Set the 'post' attribute of the tweet to the object we got earlier (the post being commented on).
        tweet.post = self.object
        
        # Assign the currently logged-in user as the author of the tweet.
        tweet.author = self.request.user
        
        # Now save the tweet object with all the added information into the database.
        tweet.save()
        
        # After saving the tweet, call the superclass's form_valid method to continue processing.
        return super().form_valid(form)

    # Override 'get_success_url' to provide the URL to redirect to after successful form submission.
    def get_success_url(self) -> str:
        # Get the current object again, which is likely to be a post instance here.
        post = self.get_object()
        
        # Use Django's reverse function to generate a URL for the single post view.
        # This assumes that there exists a URL pattern named "twitter/post_single.html" expecting a 'pk' keyword argument.
        return reverse("post_detail", kwargs={'pk': post.pk})



class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'twitter/post_update.html'
    fields = ['title', 'excerpt', 'body', 'photo']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'twitter/post_delete.html'
    success_url = reverse_lazy('home')
