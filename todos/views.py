from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from todos.models import Todo
from todos.serializers import TodoSerializer

class TodoList(generics.ListCreateAPIView):
    """
    List todos or create a new todo if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a todo item.
    """
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(owner=user)
