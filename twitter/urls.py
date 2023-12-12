from django.urls import path
from . import views

urlpatterns = [
    path('',views.messageView,name = 'message')
]
