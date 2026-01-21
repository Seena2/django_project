from . import views
from django.urls import path

urlpatterns = [
    # " " means home route
    path('',views.home, name="blog_home"),
    path('about/',views.about, name="blog_about")
]
