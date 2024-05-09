from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from posts.models import Posts
from .forms import PostsForm
from comments.models import Comments
from comments.forms import CommentForm
from categories.models import Categories
from categories.forms import CategoryForm
from django import template

register = template.Library()


def home(req):
    template_name = 'posts-list.html'
    search = req.GET.get('search')
    #paginação com o resultado da pesquisa
    if search:
        filter = Posts.objects.filter(title__icontains=search)
        paginator = Paginator(filter,3)
    #paginação a pesquisa
    else:
        all = Posts.objects.all().order_by('-create_at')
        paginator = Paginator(all,3)
    pages = req.GET.get('page')
    posts = paginator.get_page(pages)
    categories = Categories.objects.all()
    context = {
        'posts': posts,
        'categories':categories
    }
    return render(req, template_name, context)

@login_required
def perfil(req):
    template_name = 'perfil.html'
    #listar os posts do user por ordem de data
    posts = Posts.objects.all().order_by('-create_at').filter(user=req.user)
    my_categories = Categories.objects.all().filter(creator=req.user) #seleciona todas as categorias criada pelo user
    context = {
        'posts': posts,
        'my_categories': my_categories
    }
    return render(req, template_name, context)


@login_required
def create_post(req):
    template_name = 'post-form.html'
    if req.method == 'POST':
        form = PostsForm(req.POST, req.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = req.user
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:         
        form = PostsForm()
    context = {
        'form': form
    }
    return render(req, template_name, context)

def detail_post(req,id):
    template_name = 'post-detail.html'
    post = Posts.objects.get(id=id) 
    if req.method == 'POST':
        form_c = CommentForm(req.POST)
        if form_c.is_valid():
            form_c = form_c.save(commit=False)
            form_c.user = req.user
            form_c.post = post
            form_c.save()
            return HttpResponseRedirect(reverse('post-detail', args=[post.id]))
    else:         
        form_c = CommentForm()
    comments = Comments.objects.all().filter(post=post)
    context = {
        'post': post,
        'form': form_c,
        'comments': comments
    }
    return render(req, template_name, context)

@login_required
def my_comments(req):
    template_name = 'my-comments.html'
    comments = Comments.objects.all().filter(user=req.user).order_by('-create_at')
    context = {
        'comments': comments
        }
    return render(req, template_name, context)

@login_required
def delete_comment(req,id,post):
    comment = Comments.objects.get(id=id)
    comment.delete()
    return HttpResponseRedirect(reverse('post-detail', args=[post]))
    
@login_required
def update_post(req,id):
    template_name = 'post-form.html'
    post = Posts.objects.get(id=id)
    form = PostsForm(req.POST or None, req.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('post-detail', args=[post.id]))
    context = {
        'form': form
        }
    return render(req, template_name, context)

@login_required
def delete_post(req,id):
    post = Posts.objects.get(id=id) 
    post.delete()
    return HttpResponseRedirect(reverse('perfil'))


@login_required
def create_category(req):
    template_name = 'create-category.html'
    if req.method == 'POST':
        form = CategoryForm(req.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.creator = req.user
            form.save()
            return HttpResponseRedirect(reverse('perfil'))
    else:         
        form = CategoryForm()
    context = {
        'form': form
    }
    return render(req, template_name, context)


def filter_category(req,title):
    template_name='filter-category.html'
    filter = Categories.objects.get(title=title)
    categories = Categories.objects.all()
    posts = Posts.objects.all().filter(category=filter)
    context ={
        'posts': posts,
        'categories': categories,
        'filter':filter
    }
    return render(req, template_name, context)

@login_required
def delete_category(req,id):
    category = Categories.objects.get(id=id) 
    category.delete()
    return HttpResponseRedirect(reverse('perfil'))
