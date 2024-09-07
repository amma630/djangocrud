from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
#read
@api_view(['GET'])
def Booklist(request):
    booksobj=BookModel.objects.all() #queyset
    serializer=BookSerializer(booksobj,many=True)
    return Response(serializer.data)
#create
@api_view(['POST'])
def post_Book(request):
    booksobj=BookModel.objects.all() #queyset
    serializer=BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
#update
@api_view(['POST'])
def update_Book(request,id):
    booksobj=BookModel.objects.get(id=id) #queyset
    serializer=BookSerializer(instance=booksobj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
#delete
@api_view(['DELETE'])
def delete_Book(request,id):
    booksobj=BookModel.objects.get(id=id) #queyset
    booksobj.delete()
    return Response("BOOK is Deleted")