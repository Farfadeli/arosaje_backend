"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import AdviceListAPIView, AdviceDetailAPIView, AdviceCreateAPIView, AdviceUpdateAPIView, AdviceDestroyAPIView
from .views import CareListAPIView, CareDetailAPIView, CareCreateAPIView, CareUpdateAPIView, CareDestroyAPIView
from .views import CategoryListAPIView, CategoryDetailAPIView, CategoryCreateAPIView, CategoryUpdateAPIView, CategoryDestroyAPIView
from .views import PicturesListAPIView, PicturesDetailAPIView, PicturesCreateAPIView, PicturesUpdateAPIView, PicturesDestroyAPIView
from .views import PostListAPIView, PostDetailAPIView, PostCreateAPIView, PostUpdateAPIView, PostDestroyAPIView
from .views import UserListAPIView, UserDetailAPIView, UserCreateAPIView, UserUpdateAPIView, UserDestroyAPIView



urlpatterns = [
    ########## URLs des conseils #########
    path('advice/', AdviceListAPIView.as_view(), name='advice-list'),
    path('advice/<int:pk>/', AdviceDetailAPIView.as_view(), name='advice-detail'),
    path('advice/create/', AdviceCreateAPIView.as_view(), name='advice-create'),
    path('advice/<int:pk>/update/', AdviceUpdateAPIView.as_view(), name='advice-update'),
    path('advice/<int:pk>/delete/', AdviceDestroyAPIView.as_view(), name='advice-delete'),

    ########## URLs des gardes #########
    path('care/', CareListAPIView.as_view(), name='care-list'),
    path('care/<int:pk>/', CareDetailAPIView.as_view(), name='care-detail'),
    path('care/create/', CareCreateAPIView.as_view(), name='care-create'),
    path('care/<int:pk>/update/', CareUpdateAPIView.as_view(), name='care-update'),
    path('care/<int:pk>/delete/', CareDestroyAPIView.as_view(), name='care-delete'),

    ########## URLs des catégories #########
    path('category/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('category/<int:pk>/update/', CategoryUpdateAPIView.as_view(), name='category-update'),
    path('category/<int:pk>/delete/', CategoryDestroyAPIView.as_view(), name='category-delete'),

    ########## URLs des pictures #########
    path('picture/', PicturesListAPIView.as_view(), name='picture-list'),
    path('picture/<int:pk>/', PicturesDetailAPIView.as_view(), name='picture-detail'),
    path('picture/create/', PicturesCreateAPIView.as_view(), name='picture-create'),
    path('picture/<int:pk>/update/', PicturesUpdateAPIView.as_view(), name='picture-update'),
    path('picture/<int:pk>/delete/', PicturesDestroyAPIView.as_view(), name='picture-delete'),

    ########## URLs des posts #########
    path('post/', PostListAPIView.as_view(), name='picture-list'),
    path('post/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('post/create/', PostCreateAPIView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateAPIView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDestroyAPIView.as_view(), name='post-delete'),

    ########## URLs des utilisateurs #########
    path('user/', UserListAPIView.as_view(), name='picuser-list'),
    path('user/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('user/create/', UserCreateAPIView.as_view(), name='user-create'),
    path('user/<int:pk>/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('user/<int:pk>/delete/', UserDestroyAPIView.as_view(), name='user-delete'),
    

]

