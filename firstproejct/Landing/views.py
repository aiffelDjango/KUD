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
            img = request.FILES["image"].read() # 통신에서 iamge를 읽어 드리도록 한다.
            # if default_storage.exists("bfImages/"+str(img)) == False:
            #     default_storage.save("bfImages/"+str(img), img)
            convertImg = "data:image/jpg;base64, "+str(stickerGen(img)) # Html img 태그에서 출력할수 있도록 base64 타입으로 변환
            return render(request, 'Landing/stickerResult.html', {'image':convertImg}) # stickerResult.html을 보여줄때 가공한 image파일도 같이 넘긴다
        except:
            return   HttpResponse("보여줄 이미지가 없습니다!") # posㅅ
    else:
        return   HttpResponse("보여줄 이미지가 없습니다!") # pot