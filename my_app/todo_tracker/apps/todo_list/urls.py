from django.urls import path
from . import views

urlpatterns = [
    path('', views.CalenderView.as_view(), name='home'),
    path('about/', views.about, name='about'),
]
