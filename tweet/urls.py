from django.urls import path
from .views import PostListView, PostCreateView

app_name = 'tweet'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/new', PostCreateView.as_view(), name='post-create')
]
