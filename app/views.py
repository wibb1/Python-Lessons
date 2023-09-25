from django.shortcuts import get_object_or_404, render, redirect
from app import forms
from app.forms import CommentForm, NewUserForm, SubscribeForm
from app.models import Post, Comment, Tag, Profile, WebsiteMeta
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib.auth import login

def index(request):
  posts=Post.objects.all()
  top_posts=Post.objects.all().order_by('-view_count')[0:3]
  new_posts=Post.objects.all().order_by('-last_updated')[0:3]
  featured_post = Post.objects.filter(is_featured = True)
  subscribe_form = SubscribeForm()
  subscribe_successful = None
  website_info = None
  
  if WebsiteMeta.objects.all().exists():
    website_info = WebsiteMeta.objects.all()[0]
  
  if featured_post:
    featured_post = featured_post[0]
  
  if request.POST:
    subscribe_form = SubscribeForm(request.POST)
    if subscribe_form.is_valid():
      subscribe_form.save()
      request.session['subscribed'] = True
      subscribe_successful = 'Subscribed Successfully'
      subscribe_form = SubscribeForm()
  
  context={'posts': posts, "new_posts":new_posts, 'top_posts':top_posts, 'subscribe_form':subscribe_form, 'subscribe_successful':subscribe_successful, 'featured_post':featured_post, 'website_info': website_info}
  return render(request, 'app/index.html', context)

def post_page(request, slug):
  post = Post.objects.get(slug = slug)
  comments = Comment.objects.filter(post = post, parent=None)
  form = CommentForm()
  
  bookmarked = False
  if post.bookmarks.filter(id = request.user.id).exists():
    bookmarked = True
  is_bookmarked = bookmarked
  
  if request.POST:
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid:
      # parent_obj = None
      if request.POST.get('parent'):
        parent = request.POST.get('parent')
        parent_obj = Comment.objects.get(id=parent)
        if parent_obj:
          comment_reply = comment_form.save(commit=False)
          comment_reply.parent = parent_obj
          comment_reply.post = post
          comment_reply.save()
      else:  
        comment = comment_form.save(commit=False)
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id = post_id)
        comment.post = post
        comment.save()
      return HttpResponseRedirect(reverse('post_page', kwargs={'slug':slug}))
  
  if post.view_count is None:
    post.view_count = 1
  else:
    post.view_count = post.view_count + 1
  post.save()
  
  context = {'post': post, 'form':form, 'comments':comments, 'is_bookmarked':is_bookmarked}
  return render(request, 'app/post.html', context)

def tag_page(request, slug):
  tag = Tag.objects.get(slug=slug)
  top_posts = Post.objects.filter(tags__in=[tag.id]).order_by('-view_count')[0:2]
  new_posts = Post.objects.filter(tags__in=[tag.id]).order_by('-last_updated')[0:2]
  tags = Tag.objects.all()
  context = {'tag':tag, 'top_posts':top_posts, 'new_posts':new_posts, 'tags':tags}
  return render(request, 'app/tag.html', context)

def author_page(request, slug):
  profile = Profile.objects.get(slug=slug)
  top_posts = Post.objects.filter(author=profile.user).order_by('-view_count')[0:2]
  new_posts = Post.objects.filter(author=profile.user).order_by('-last_updated')[0:2]
  top_authors = User.objects.annotate(number=Count('post')).order_by('-number')[0:2]
  
  context = {'profile': profile, 'top_posts':top_posts, 'new_posts':new_posts, 'top_authors':top_authors}
  return render(request, 'app/author.html', context)

def search_posts(request):
  search_query = request.GET.get('q') if request.GET.get('q') else ''
  posts = Post.objects.filter(title__icontains=search_query)
  context = {'posts':posts, 'search_query':search_query}
  return render(request, 'app/search.html', context)

def about(request):
  website_info = None
  if WebsiteMeta.objects.all().exists():
    website_info = WebsiteMeta.objects.all()[0]
  context = {'website_info':website_info}
  return render(request, 'app/about.html', context)
  
def register_user(request):
  form = NewUserForm()
  if request.method =='POST':
    form = NewUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/')
  context = {'form': form}
  return render(request, 'registration/registration.html', context)

def clean_username(self):
  username = self.cleaned_data['username'].lower()
  new = User.objects.filter(username = username)
  if new.count():
    raise forms.ValidationError('User already exists')
  return username

def clean_email(self):
  email = self.cleaned_data['email'].lower()
  new = User.objects.filter(email = email)
  if new.count():
    raise forms.ValidationError('Email already exists')
  return email

def clean_password2(self):
  password1 = self.cleaned_data['password1']
  password2 = self.cleaned_data['password2']
  if password1 and password2 and password2 != password1:
    raise forms.ValidationError('Passwords must be the same')
  return password2

def bookmark_post(request, slug):
  post = get_object_or_404(Post, id=request.POST.get('post_id'))
  if post.bookmarks.filter(id=request.user.id).exists():
    post.bookmarks.remove(request.user)
  else:
    post.bookmarks.add(request.user)
  return HttpResponseRedirect((reverse('post_page', args=[str(slug)])))
