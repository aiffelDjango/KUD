from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView

# Create your views here.
@api_view(['GET','POST'])
def fun_calc_add(request):
    if request.method == 'GET':
        return Response("Add Get")

    if request.method == 'POST':
        num1 = request.data["num1"]
        num2 = request.data["num2"]
        return Response({"message": "Got some data!", "mathematical expression" : " %d + %d "%(num1,num2) ,"result": num1+num2})

@api_view(['GET','POST'])
def fun_calc_sub(request):
    if request.method == 'GET':
        return Response("Sub Get")
    if request.method == 'POST':
        num1 = request.data["num1"]
        num2 = request.data["num2"]
        return Response({"message": "Got some data!", "mathematical expression" : " %d - %d "%(num1,num2) ,"result": num1-num2})


@api_view(['GET','POST'])
def fun_calc_mul(request):
    if request.method == 'GET':
        return Response("Mul Get")
    if request.method == 'POST':
        num1 = request.data["num1"]
        num2 = request.data["num2"]
        return Response({"message": "Got some data!", "mathematical expression" : " %d * %d "%(num1,num2) ,"result": num1*num2})

@api_view(['GET','POST'])
def fun_calc_div(request):
    if request.method == 'GET':
        return Response("Div Get")
    if request.method == 'POST':
        num1 = request.data["num1"]
        num2 = request.data["num2"]
        return Response({"message": "Got some data!", "mathematical expression" : " %d / %d "%(num1,num2) ,"result": num1/num2})


class class_add(APIView):
    def get(self, request):
        return Response("Add Get")
    def post(self, request):
        num1 = request.data["num1"]
        num2 = request.data["num2"]
        return Response({"message": "Got some data!", "mathematical expression" : " %d + %d "%(num1,num2) ,"result": num1+num2})
      
class class_sub(APIView):
    def get(self, request):
        return Response("Sub Get")
    def post(self, request):
        num1 = request.data["num1"]
        num2 = request.data["num2"]
        return Response({"message": "Got some data!", "mathematical expression" : " %d - %d "%(num1,num2) ,"result": num1-num2})
    
class class_mul(APIView):
    def get(self, request):
        return Response("Mul Get")
    def post(self, request):
        num1 = request.data["num1"]
        num2 = request.data["num2"]
        return Response({"message": "Got some data!", "mathematical expression" : " %d * %d "%(num1,num2) ,"result": num1*num2})
      
class class_div(APIView):
    def get(self, request):
        return Response("div Get")
    def post(self, request):
        num1 = request.data["num1"]
        num2 = request.data["num2"]
        return Response({"message": "Got some data!", "mathematical expression" : " %d / %d "%(num1,num2) ,"result": num1/num2})
