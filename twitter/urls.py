from django.urls import path
from .views import HomeView, NewPostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/new',NewPostView.as_view(), name = 'newpost'),
]
