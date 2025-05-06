from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    blog_create,
    blog_list,
    blog_detail_view,
    blog_update,
    blog_delete,
    tag_create,
    tag_list,
    tag_update,
    tag_delete
)

app_name = 'blog'

urlpatterns = [
    path('blog_create/', blog_create, name='blog_create'),
    path('blog_list/', blog_list, name='blog_list'),
    path('blog_detail_view/<int:id>', blog_detail_view, name='blog_detail_view'),
    path('blog/<int:pk>/edit/', blog_update, name='blog_update'),
    path('blog/<int:pk>/delete/', blog_delete, name='blog_delete'),

    path('tag_create/', tag_create, name='tag_create'),
    path('tag_list/', tag_list, name='tag_list'),
    path('tag/<int:pk>/edit/', tag_update, name='tag_update'),
    path('tag/<int:pk>/delete/', tag_delete, name='tag_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)