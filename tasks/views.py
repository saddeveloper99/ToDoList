from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from tasks.serializers import TaskCreateSerializer, TaskSerializer
from tasks.models import Task


class TaskView(APIView):
    def get(self, request):
        task_list = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(task_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


