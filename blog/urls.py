from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('explore/', views.ExplorePostListView.as_view(), name='explore'),
    path('my_blog/', views.MyblogPostListView.as_view(), name='my_blog'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts_by_/<str:username>/', views.UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('contact/', views.contact, name='blog-contact'),
    path('category/<str:cat>', views.blog_by_category.as_view(), name='blog-category'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)