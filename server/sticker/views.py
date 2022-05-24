from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from .models import imagePost
from rest_framework import status

# Create your views here.

# @api_view(['GET','POST'])
# def stickerResult(request):
#     if request.method == 'GET':
#         return Response("Image를 보여줄게")
#
#     if request.method == 'POST':
#         try:
#             imgMemory = request.FILES[
#                 "image"
#             ]  # 통신에서 iamge를 inmemory에 저장되어 있는 값으로 읽어 드리도록 한다.
#             imgByte = imgMemory.read()  # 통신에서 iamge를 Byte로 읽어 드리도록 한다.
#             convertImg = "data:image/jpg;base64, " + str(
#                 stickerGen(imgByte)
#             )  # Html img 태그에서 출력할수 있도록 base64 타입으로 변환
#             return Response()  # stickerResult.html을 보여줄때 가공한 image파일도 같이 넘긴다
#         except:
#             return Response("보여줄 이미지가 없습니다!")  # image 파일이 없으면 처리
#     else:
#         return Response("보여줄 이미지가 없습니다!")  # post 통신이 아니면 자료를 보낼수 없어서 예외 처리

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


# class PostView(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#     def get(self, request, *args, **kwargs):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         posts_serializer = PostSerializer(data=request.data)

#         if posts_serializer.is_valid():
#             posts_serializer.save()
#             return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             print('error', posts_serializer.errors)
#             return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
