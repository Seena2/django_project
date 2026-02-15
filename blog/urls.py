from django.urls import path
from . import views
from .views import PostListView,PostDetailView, PostCreateView,PostUpdateView,PostDeleteView, UserPostListView

urlpatterns = [ 
    # path('',views.home, name="blog_home"), # " " means home route 
    path('',PostListView.as_view(), name="blog_home"), 
    path('about/',views.about, name="blog_about"),
    path('post/<int:pk>/',PostDetailView.as_view(), name="post_detail"), #Parameterized route
    path('post/new/',PostCreateView.as_view(), name="post_create"), 
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name="post_update"), #Parameterized route
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name="post_delete"),
    path('user/<str:username>',UserPostListView.as_view(), name="user_posts"), 
]
