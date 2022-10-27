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
    List all code blogs, or create a new snippet.
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
    
    
