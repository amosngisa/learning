from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog_list, name='blog'),
    path('subscribe/', views.subscriber, name='subscribe'),
    path('add_blog/', views.add_blog, name='add_blog'),
]
