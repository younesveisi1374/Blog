from django.urls import path
from .views import HomeView, NewPostView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/new', NewPostView.as_view(), name='newpost'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
