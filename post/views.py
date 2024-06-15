from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView

from rest_framework.viewsets import ModelViewSet
from .models import TodoModel
from .serializers import PostSerializers


class ListTodo(ListAPIView):
    queryset=TodoModel.objects.all()
    serializer_class=PostSerializers


class RetrieveTodo(RetrieveAPIView):
    queryset=TodoModel.objects.all()
    serializer_class=PostSerializers
    lookup_field='pk'

class CreateTodo(CreateAPIView):
    queryset=TodoModel.objects.all()
    serializer_class=PostSerializers

class DeleteTodo(DestroyAPIView):
    queryset=TodoModel.objects.all()
    serializer_class=PostSerializers
    lookup_field='pk'


class UpdateTodo(UpdateAPIView):
    queryset=TodoModel.objects.all()
    serializer_class=PostSerializers
    lookup_field='pk'












# Create you views here.
