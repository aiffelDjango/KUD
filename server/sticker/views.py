from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from .models import imagePost
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])

def stickerResult(request):
    if request.method == 'GET':
        posts = imagePost.objects.all()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
         posts_serializer = PostSerializer(data=request.data)

         if posts_serializer.is_valid():
             posts_serializer.save()
             return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
         else :
             print('error',posts_serializer.errors)
             return Response(posts_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
