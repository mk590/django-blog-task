from django.shortcuts import render,redirect,HttpResponse

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
        # Blog = Blog.objects.get(pk=pk)
        blog = Blog.objects.get(pk=pk)
    except blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = blogSerializer(blog)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = blogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
from .forms import *
    
@api_view(['GET','POST'])
def Form(request):
    if request.method=='POST':
        formdata = blogForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            # return Response("saved")
            # return render()
            return redirect("/show")
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
 
 
def View_blog(request,pk):
    # try:
        content = Blog.objects.get(pk= pk)
        info = {'content' : content }
        return render(request,"view_blog.html",info)
    # except:
    #     return HttpResponse("Some error occurred while processing your request")
    
    
    # how the updation works
def Update(request,pk):
    try:
        if request.method == "POST":
            particularBlog = Blog.objects.get(pk= pk)
            update = blogForm(request.POST, request.FILES ,instance = particularBlog)
            if update.is_valid():
                update.save()
                return redirect("/show")
            
        particularBlog = Blog.objects.get(pk= pk)
        content = blogForm(instance=particularBlog)
        info = {'content':content}
        # return render(request,"update.html",info)
        return render(request,"new_blog.html",info)
    except:
        return HttpResponse("Some error occurred while processing your request")


def Delete(request,pk):
    try:
        particularBlog = Blog.objects.get(pk= pk)
        particularBlog.delete()
        return redirect("/show")
    except:
        return 