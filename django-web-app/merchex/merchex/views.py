from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Advice, Care, Category, Pictures, Post, User
from rest_framework import generics
from .serializers.advice_serializer import AdviceSerializer
from .serializers.care_serializer import CareSerializer
from .serializers.category_serializer import CategorySerializer
from .serializers.picture_serializer import PictureSerializer
from .serializers.post_serializer import PostSerializer
from .serializers.user_serializer import UserSerializer



########## Vues des conseils #########

class AdviceListAPIView(generics.ListAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer

class AdviceDetailAPIView(generics.RetrieveAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer
    
class AdviceCreateAPIView(generics.CreateAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer

class AdviceUpdateAPIView(generics.UpdateAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer
    
class AdviceDestroyAPIView(generics.DestroyAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer


########## Vues des gardes #########

class CareListAPIView(generics.ListAPIView):
    queryset = Care.objects.all()
    serializer_class = CareSerializer

class CareDetailAPIView(generics.RetrieveAPIView):
    queryset = Care.objects.all()
    serializer_class = CareSerializer
    
class CareCreateAPIView(generics.CreateAPIView):
    queryset = Care.objects.all()
    serializer_class = CareSerializer

class CareUpdateAPIView(generics.UpdateAPIView):
    queryset = Care.objects.all()
    serializer_class = CareSerializer
    
class CareDestroyAPIView(generics.DestroyAPIView):
    queryset = Care.objects.all()
    serializer_class = CareSerializer
    
    
########## Vues des category #########

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

########## Vues des pictures #########

class PicturesListAPIView(generics.ListAPIView):
    queryset = Pictures.objects.all()
    serializer_class = PictureSerializer

class PicturesDetailAPIView(generics.RetrieveAPIView):
    queryset = Pictures.objects.all()
    serializer_class = PictureSerializer
    
class PicturesCreateAPIView(generics.CreateAPIView):
    queryset = Pictures.objects.all()
    serializer_class = PictureSerializer

class PicturesUpdateAPIView(generics.UpdateAPIView):
    queryset = Pictures.objects.all()
    serializer_class = PictureSerializer
    
class PicturesDestroyAPIView(generics.DestroyAPIView):
    queryset = Pictures.objects.all()
    serializer_class = PictureSerializer
    
    
########## Vues des posts #########

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostDestroyAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
########## Vues des user #########

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    

    
    
    
    


    
    
