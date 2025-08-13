from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def comment_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('posts:page', slug=post.slug)
        else:
            return render(request, 'posts/post_page.html', {'post': post, 'form': form})
    else:
        form = forms.CommentForm()
    return render(request, 'posts/post_page.html', {'post': post, 'form': form})

def like_post(request, post_id):
    if not request.user.is_authenticated:
        return redirect('users:login')
    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=request.user.id):
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('posts:page', slug=post.slug)

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('posts:list')
    return render(request, 'posts/confirm_delete.html', {'post': post})

def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = forms.EditPost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            update_post = form.save(commit=False)
            update_post.title = post.title 
            update_post.save()
            return redirect('posts:page', slug=post.slug)
        else:
            return render(request, 'posts/edit_post.html', {'form': form, 'post': post})
    else:
        form = forms.EditPost(instance=post)
    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})

def post_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})

def post_page(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by('-date')
    return render(request, 'posts/post_page.html', {'post': post, 'comments': comments})

@login_required(login_url="users:login")
def post_new(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', { 'form': form }) 