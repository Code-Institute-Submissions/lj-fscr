from . import views
from django.urls import path


urlpatterns = [
    path('', views.all_posts, name='forum'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('add_post', views.add_post, name='add_post'),
]