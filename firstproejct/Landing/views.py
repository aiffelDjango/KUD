from django.shortcuts import render

# Create your views here.
def study(req):
    return render(req,'Landing/study.html')

def index(req):
    return render(req,'Landing/index.html')