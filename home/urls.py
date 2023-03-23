from django.urls import path 
from . import views 
urlpatterns = [ 
path('home/', views.index),
path('tintuc', views.index2),
path('contact', views.index3),
]