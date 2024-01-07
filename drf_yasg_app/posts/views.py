from rest_framework import viewsets
from posts.models import Post
from posts.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint for posts
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
