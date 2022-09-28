from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from api_blog.serializers import BlogAPI
from api_blog.models import Blog
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class BlogCreateAPIView(APIView):
    def get(self, request):
        blog = Blog.objects.all()
        serializer = BlogAPI(blog, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = BlogAPI(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogUpdateAPIView(APIView):

    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogAPI(blog)
        return Response(serializer.data)
    
    def put(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogAPI(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)