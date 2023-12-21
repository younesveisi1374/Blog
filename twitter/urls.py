from django.urls import path
from .views import HomeView, NewPostView, PostDetailView, PostUpdateView, PostDeleteView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/new', NewPostView.as_view(), name='newpost'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/update/<int:pk>',PostUpdateView.as_view(),name = 'post_update'),
    path('post/delete/<int:pk>',PostDeleteView.as_view(),name = 'post_delete'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
