from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import ToDo, Tag
from .serializers import ToDoSerializer


class ToDoModelViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
