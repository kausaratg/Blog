from django.urls import path
from api_blog.views import BlogCreateAPIView, BlogUpdateAPIView

urlpatterns = [
    path('', BlogCreateAPIView.as_view()),
    path('<int:pk>', BlogUpdateAPIView.as_view())
]
