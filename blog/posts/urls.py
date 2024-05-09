from django.urls import path
from .views import home, perfil ,create_post, update_post, detail_post, my_comments, delete_comment, delete_post, create_category, filter_category, delete_category

urlpatterns = [
    path('', home, name='home'),
    path('perfil/', perfil, name='perfil'),
    path('create/', create_post, name='post-create'),
    path('post/<int:id>', detail_post, name='post-detail'),
    path('comments/', my_comments, name='my-comments'),
    path('<int:post>/comment/<int:id>', delete_comment, name='delete-comment'),
    path('update/<int:id>', update_post, name='post-update'),
    path('delete/<int:id>', delete_post, name='post-delete'),
    path('category/', create_category, name='create-category'),
    path('filter/<str:title>', filter_category, name='filter-category'),
    path('category/<int:id>', delete_category, name='delete-category')
]
