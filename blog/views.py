from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['GET', 'POST'])
def blog_list(request):
    """
    List all code blogs, or create a new Blog.
    """
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = blogSerializer(blogs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = blogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def blog_detail(request, pk):
    """
    Retrieve, update or delete a blog.
    """
    try:
        Blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = blogSerializer(Blog)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = blogSerializer(Blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
from .forms import *
    
@api_view(['GET','POST'])
def Form(request):
    if request.method=='POST':
        formdata = blogForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            return Response("saved")
        return Response("not saved")
    
    content = blogForm()
    info = {'content':content}
    return render(request,"new_blog.html",info)


# AssertionError at /form/
# .accepted_renderer not set on Response
# this was the error i got when i was doing withoit the api decorater in this case 


# @api_view(['GET','POST'])
def show(request):
     blogs = Blog.objects.all()
     return render(request,"blog_display.html",{'info':blogs})