from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer, AuthorSerializer, OrderSerializer, CustomUserSerializer

from book.models import Book
from author.models import Author
from order.models import Order
from authentication.models import CustomUser

model = {
    'user': [CustomUser, CustomUserSerializer],
    'book': [Book, BookSerializer],
    'author': [Author, AuthorSerializer],
    'order': [Order, OrderSerializer]
}


@api_view(['GET'])
def view_all(request, ob):
    path = model[ob]
    tasks = path[0].objects.all().order_by('-id')
    serializer = path[1](tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def view_id(request, ob, pk):
    path = model[ob]
    tasks = path[0].objects.get(id=pk)
    serializer = path[1](tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create(request, ob):
    path = model[ob]
    serializer = path[1](data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def update(request, ob, pk):
    path = model[ob]
    task = path[0].objects.get(id=pk)
    serializer = path[1](instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete(request, ob, pk):
    path = model[ob]
    task = path[0].objects.get(id=pk)
    task.delete()
    return Response('Item succsesfully delete!')


@api_view(['GET'])
def view_order_all(request, id):
    tasks = Order.objects.filter(user=id)
    serializer = OrderSerializer(tasks, many=True)
    return Response(serializer.data)