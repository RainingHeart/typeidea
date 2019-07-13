from rest_framework import viewsets

from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(status=Comment.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CommentDetailSerializer
        return super().retrieve(request, *args, **kwargs)
