from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm, CommentsForm
from django.urls import reverse_lazy

# Create your views here.
class AboutView(TemplateView):
    template_name = "about.html"

class PostListView(ListView):
    model = Post

    def get_query_set(self):
        return Post.objects.filter(published_date__lte=timezone.now.order_by('-published_date'))
    
class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = "blog/post_detail.html"

    form_class = PostForm
    model = Post

class PostUpdateView(UpdateView):
    login_url = '/login/'
    redirect_field_name = "blog/post_detail.html"

    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")

class DraftListView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    redirect_field_name = "blog/post_list.html"
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by("created_date")
    
@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.metthod == "POST":
        form = CommentsForm(request.POST)