from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'user_id', 'created_at', 'updated_at']

# ViewSets define the view behavior.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer