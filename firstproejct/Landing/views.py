from django.shortcuts import render
from django.core.files.storage import default_storage
import tempfile


# Create your views here.
def index(req):
    return render(req,'Landing/index.html')

def sticker(req):
    return render(req,'Landing/sticker.html')

def study(req):
    return render(req,'Landing/study.html')


def stickerResult(request):
    if request.method == 'POST':
        img = request.FILES["image"]
        if default_storage.exists("bfImages/"+str(img)) == False:
            default_storage.save("bfImages/"+str(img), img)
        tmpResult = 
        return render(request, 'Landing/stickerResult.html', {'image':img})
    else:
        return render(request, 'Landing/stickerResult.html')