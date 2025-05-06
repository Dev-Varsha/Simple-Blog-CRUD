from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Tag
from .forms import BlogForm, TagForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
@login_required(login_url="login")
@permission_required(["blog.add_blog"],
                      raise_exception=True)
def blog_create(request):
    ""
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog/blog_creation.html', {'form': form, 'title': 'Create blog'})

@login_required(login_url="login")
@permission_required(["blog.view_blog"],
                      raise_exception=True)
def blog_list(request):
    query = request.GET.get('q')
    view_type = request.GET.get('view', 'list')
    blog_list = Blog.objects.all()

    if query:
        blog_list = blog_list.filter(Q(title__icontains=query))

    paginator = Paginator(blog_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/blog_list.html', {
        'page_obj': page_obj,
        'query': query,
        'view_type': view_type
    })

@login_required(login_url="login")
@permission_required(["blog.view_blog"],
                      raise_exception=True)
def blog_detail_view(request, id):
    ""
    detail_view = Blog.objects.get(id=id)
    return render(request, 'blog/blog_detail_view.html', {'detail_view':detail_view})

@login_required(login_url="login")
@permission_required(["blog.change_blog"],
                      raise_exception=True)
def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog:blog_list')
    else:
        form = BlogForm(instance=blog)
        form.fields['tags'].initial = blog.tags.all()
    return render(request, 'blog/blog_creation.html', {'form': form, 'title': 'Update blog'})

@login_required(login_url="login")
@permission_required(["blog.delete_blog"],
                      raise_exception=True)
def blog_delete(request, pk):
    ""
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog:blog_list')
    return render(request, 'blog/blog_confirm_delete.html', {'blog': blog})

# ======================================================= TAG CRUD ==============================================================

@login_required(login_url="login")
@permission_required(["blog.add_tag"],
                      raise_exception=True)
def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:tag_list')
    else:
        form = TagForm()
    return render(request, 'blog/tag_creation.html', {'form': form, 'title': 'Create Tag'})

@login_required(login_url="login")
@permission_required(["blog.view_tag"],
                      raise_exception=True)
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', {'tags': tags})

@login_required(login_url="login")
@permission_required(["blog.change_tag"],
                      raise_exception=True)
def tag_update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('blog:tag_list')
    else:
        form = TagForm(instance=tag)
    return render(request, 'blog/tag_creation.html', {'form': form, 'title': 'Edit Tag'})

@login_required(login_url="login")
@permission_required(["blog.delete_tag"],
                      raise_exception=True)
def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('blog:tag_list')
    return render(request, 'blog/tag_confirm_delete.html', {'tag': tag})