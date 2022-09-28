from rest_framework import serializers
from api_blog.models import Blog

class BlogAPI(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"