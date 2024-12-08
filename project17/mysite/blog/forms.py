from django import forms
from blog.models import Post, Comments

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("author", "title", "text")

class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("author", "text")