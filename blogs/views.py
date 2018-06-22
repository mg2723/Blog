from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm


def index(request):
    return render(request, 'blogs/index.html')


def check_blog_owner(request, blog):
    if blog.owner != request.user:
        raise Http404


def topics(request):
    topics = BlogPost.objects.order_by('-date_added')
    context = {'topics': topics}
    return render(request, 'blogs/topics.html', context)


@login_required
def new_blog(request):
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return HttpResponseRedirect(reverse('blogs:topics'))

    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)


@login_required
def edit_blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    check_blog_owner(request, blog)
    if request.method != 'POST':
        form = BlogPostForm(instance=blog)
    else:
        form = BlogPostForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:topics'))

    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)
