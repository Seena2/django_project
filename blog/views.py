from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView, CreateView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Function based Views
def home(request):
    # return HttpResponse ("<h1>Blogs Home</h1>")
    context={
        # 'posts':posts // passing dummy data
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html', context)

def about(request):
   return render(request,'blog/about.html',{'title':"About"})

# Class-based views
# List all the posts 
class PostListView(ListView):
    model=Post
    template_name="blog/home.html" #<app>/<model>_<viewtype>.html
    context_object_name='posts'
    ordering=['-date_posted'] # "-" orders posts in descending order
    paginate_by=5

# List all the posts by single author 
class UserPostListView(ListView):
    model=Post
    template_name="blog/user_posts.html"
    context_object_name='posts'
    paginate_by=5

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')# "-" orders posts in descending order


# Detail for specific post
class PostDetailView(DetailView):
    model=Post

# Create new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

# Update post
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Delete specific post
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
   
  

