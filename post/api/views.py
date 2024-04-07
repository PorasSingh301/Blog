from post.models import Post, Comment
from rest_framework import permissions, viewsets, generics, status
from rest_framework.decorators import action

from post.api.serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response


class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['put', "patch"])
    def like(self, request, pk=None):
        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return Response({"error": "post does not exist"}, status=status.HTTP_404_NOT_FOUND)
        post.like_a_post()
        return Response(self.serializer_class(post).data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def count_likes(self, request, pk=None):
        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return Response({"error": "post does not exist"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"likes": post.likes}, status=status.HTTP_200_OK)


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

