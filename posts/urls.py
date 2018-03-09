from django.urls import path, include
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostListView.as_view(), name='list'),
    path('new/', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
]
