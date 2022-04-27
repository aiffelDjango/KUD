from django.shortcuts import render
from django.core.files.storage import default_storage
from django.http import HttpResponse
import tempfile
from stickerUtil.sticker import stickerGen


# Create your views here.
def index(req):
    return render(req,'Landing/index.html')

def sticker(req):
    return render(req,'Landing/sticker.html')

def study(req):
    return render(req,'Landing/study.html')


def stickerResult(request):
    if request.method == 'POST': # 통신이 post일때
        try:
            imgByte = request.FILES["image"].read() # 통신에서 iamge를 읽어 드리도록 한다.
            imgMemory= request.FILES["image"] # 통신에서 iamge를 읽어 드리도록 한다.
            if default_storage.exists("bfImages/"+str(imgMemory)) == False:
                default_storage.save("bfImages/"+str(imgMemory), imgMemory)
            convertImg = "data:image/jpg;base64, "+str(stickerGen(imgByte)) # Html img 태그에서 출력할수 있도록 base64 타입으로 변환
            return render(request, 'Landing/stickerResult.html', {'image':convertImg}) # stickerResult.html을 보여줄때 가공한 image파일도 같이 넘긴다
        except:
            return   HttpResponse("보여줄 이미지가 없습니다!") # image 파일이 없으면 처리
    else:
        return   HttpResponse("보여줄 이미지가 없습니다!") # post 통신이 아니면 자료를 보낼수 없어서 예외 처리