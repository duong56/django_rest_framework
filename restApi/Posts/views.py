from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # permission_classes = [permissions.IsAuthenticated]
    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
