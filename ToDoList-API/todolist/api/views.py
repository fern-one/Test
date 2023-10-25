from .models import Task
from rest_framework import viewsets
from api.serializers import TaskSerializer


class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
