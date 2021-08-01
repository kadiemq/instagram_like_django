from rest_framework.generics import RetrieveUpdateDestroyAPIView, get_object_or_404, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from commentApp.models import Comment
from commentApp.serializer import CommentSerializer


class ListCreateComment(ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    filter_kwargs = 'post'

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, post=self.kwargs['pk'])
        return obj


class RetrieveUpdateDeleteComment(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
