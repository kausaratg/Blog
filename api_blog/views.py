from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api_blog.serializers import BlogAPI
from api_blog.models import Blog

# Create your views here.
class BlogCreateAPIView(ListCreateAPIView):
    serializer_class = BlogAPI
    def get_queryset(self):
        return Blog.objects.all()

class BlogUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogAPI

    def get_queryset(self):
        return Blog.objects.all()
