from django.shortcuts import render
from .models import Post, Comment
from django.views.generic import TemplateView, ListView
from django.utils import timezone

# Create your views here.
class AboutView(TemplateView):
    template_name = "about.html"

class PostListView(ListView):
    model = Post

    def get_query_set(self):
        return Post.objects.filter(published_date__lte=timezone.now.order_by('-published_date'))