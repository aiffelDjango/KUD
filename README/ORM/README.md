# Django에서 SQL 사용기

## Project Setting

- 복습을 위해 `Django`의 프로젝트를 다시 생성 해보도록 하겠습니다.

- 그럼 가상 환경을 위해 `virtual environment`를 위해 `venv` 설정을 해보도록 하겠습니다.

```console
# myvenv를 설정

python -m venv myvenv
```

- `pip`를 업그레이드를 진행하고, `django`를 설치하겠습니다.

```console
# venv Start
.\myvenv\Scripts\activate

# pip upgrade
python -m pip install --upgrade pip

# django install
pip install django
```

- `django-admin`을 통해 `django` 프로젝트 생성하겠습니다.

```console
# django Project RestAPI
django-admin startproject RestAPI

# Entry RestAPI folder
cd RestAPI

```

## REST API

- 앞서 `Figma`를 통해 `REST API`에 대해 어느정도 설명을 드렸다고 생각합니다.

- `Django`에서 `REST API`를 다루기 쉽게 하기 위한 라이브러리인 `Django REST framework` 를 설치해볼 시간입니다.

```console
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```

- 그리고 해당 라이브러리를 `settings.py`에서 추가해주도록 하겠습니다.

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', # Rest FrameWork
]
```

- `REST API`를 테스트하기 위해 `Calculator`라는 `App`을 만들도록 하겠습니다.

```console
python ./manage.py startapp Calculator
```

- `views.py`에서 `Calculator`라는 `API`를 구성해보도록 하겠습니다.

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', # Rest FrameWork
    'Calculator', # App Name Calculator
]
```

- 구성 방법은 `FBV(함수기반뷰)`,`CBV(클래스기반뷰)` 두가지가 있습니다.

- 먼저 `FBV`방식으로 `POST`를 통해 숫자를 받고 결과를 배출하는 수식을 만들어 보도록 하겠습니다.

```py

@api_view(['GET','POST']) #
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
```

- 먼저 `CBV`방식으로 `POST`를 통해 숫자를 받고 결과를 배출하는 수식을 만들어 보도록 하겠습니다.

```py

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

```

## SQL

- `sql`이라는 이름의 `APP`을 만들어보도록 하겠습니다.

```console
# django App create
python ./manage.py startapp sql
```

- `App`을 프로젝트에서 인식할수 있도록 `setting.py`애 `INSTALLED_APPS`부분의 `App`이름을 적어 주도록 하겠습니다.

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework', # Rest FrameWork
    'Calculator', # App Name Calculator
    'sql', # App Name Calculator
]
```

## sql 프로젝트 세팅

- 이제 우리의 본 프로젝트인 `mysql`를 `djnago`에서 사용하는 프로젝트를 진행하도록 하겠습니다!

- `mysql`과 `django`를 연결하는 `Databaser Connector`를 설치 하겠습니다.

```py
# Mysql Install Databser Connector
pip install mysqlclient

# MAC Install MysqlClient
brew install mysql-client
echo 'export PATH="/usr/local/opt/mysql-client/bin:$PATH"' >> ~/.bash_profile
export PATH="/usr/local/opt/mysql-client/bin:$PATH"
pip install mysqlclient
```

- 이제 `manage.py`가 있는 폴더에 `mysql_setting.py`를 만들어주시고 아래 내용을 쳐주시면 됩니다.

```py
DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql', # 사용할 DBMS
        'NAME' : 'test', # Mysql 데이터베이스 이름
        'USER' : 'root', # DB 접속 계정명
        'password': '1q2w3e', # 해당 계정의 비밀번호
        'HOST' : '146.56.154.230', # IP
        'PORT' : '3306' # PORT
    }
}
SECRET_KEY = 'django-insecure-r-9u+%7ln=dl78q90xx+lkw0c1vlajxi*h^8n7j)!9p6k2&dh%' # 시크릿 key
```

- 해당 내용들은 `DB`폴더에 있는 `settings.py`의 `DATABASES`와 `SECRET_KEY`를 설정합니다.

- 그럼 설정을 했기 때문에 필요없어진 `settings.py`에 있는 `DATABASES`와 `SECRET_KEY`를 지우고 `mysql_setting.py`에 있는 내용으로 바꾸겠습니다.

```py
# settings.py
import mysql

SECRET_KEY = mysql.SECRET_KEY # 기존에 있던 SECRET_KEY를 분리

DATABASES = mysql.DATABASES  # 기존에 있던 DATABASES를 mysql_setting에 SECRET_KEY

```

- 이제 `mysql`과 `Django`를 연결이 되는지 보겠습니다.

```console
python manage.py insepctdb
```

<p align="center"><img src="./IMG/1.png "></p>

- `mysql`에 있는 `table`을 python코드로 올려줍니다.

- 나온 코드를 복사해서 `App(sql)`의 `model.py` 넣어주시면 됩니다.

- 왜 넣어주는지는 나중에 설명하도록 하겠습니다.

## Django에서 sql 사용하기

- 그전에 `create`를 통해 테이블을 만들필요가 있습니다.

```sql
CREATE TABLE tmp (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50),age INT);
```

- `views.py`에서 `create`라는 함수를 만들고 `url(127.0.0.1:8000)`을 들어갈때 `views.py`에 우리가 정의한 함수를 실행 시켜 `table`을 생성하겠습니다.

```py
def sqlExcuter(sql):
    try:
        cursor = connection.cursor() # mysql에 접속을 위한 객체 생성
        result = cursor.execute(sql) # sql을 수행
        datas = cursor.fetchall() # DB에서 수행하고 나온 결과물을 반환

        connection.commit() # DB에 대한 변경사항 확정 및 갱신
        connection.close() # DB 연결 닫음
        return datas

    except Exception as ex:
        connection.rollback()
        return ("Fail to sql, the string is" + sql + "error: " + str(ex))

def create(request):
    mysql = "CREATE TABLE tmp (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50),age INT);"
    result = sqlExcuter(mysql)
    return HttpResponse(result)
```

- cursor(): cursor 객체 (SQL문을 수행하고 결과를 얻는데 사용하는 객체)생성

- cursor.execute(): 쿼리문을 연결된 DB로 보내 쿼리를 실행

- cursor.fetchall(): 쿼리 실행 결과로 반환된 전체 데이터를 데이터베이스 서버로부터 가져옴

- connection: 데이터베이스에 접속을 하기 위한 모듈

- connection.commit(): 데이터에 대한 변경사항이 있다면 이를 확정, 갱신

- connection.close(): 데이터베이스와의 연결을 닫힘

- connection.rollback(): 쿼리문 실행 도중 잘못된 경우 실행 전으로 되돌려 놓음

- 이제 `Table`에 대한 `CRUD`를 함수들을 만들고 마찬가지로 `views.py`에 우리가 정의한 함수를 실행 시켜 `DB`에 반영해보도록 하겠습니다.

- `views.py`에서 먼저 `CRUD`,함수들은 `sql`만 바꾸고 간단하게 만들었습니다. (해당 sql을 바꾸셔도 상관없습니다)

```py

#Create
def insert(request):
    mysql = " INSERT INTO tmp(ID, Name, age) VALUES(2, 'KUD2', '3'); "
    result = sqlExcuter(mysql)
    return HttpResponse(result)

#Read
def select(request):
    mysql = "select * from tmp;"
    result = sqlExcuter(mysql)
    return HttpResponse(result)

#Update
def update(request):
    mysql = "UPDATE tmp SET age = 2002 WHERE id = 1;"
    result = sqlExcuter(mysql)
    return HttpResponse(result)

#Delete
def delete(request):
    mysql = " DELETE FROM tmp WHERE Name = 1;"
    result = sqlExcuter(mysql)
    return HttpResponse(result)
```

- 두번째는 만든 함수들을 호출하는 `url` 4가지를 설정을 해야합니다.

- `url(127.0.0.1:8000)/insert`,`url(127.0.0.1:8000)/update`,`url(127.0.0.1:8000)/delete`,`url(127.0.0.1:8000)/create`

- `urls.py`에서 코드를 작성해 주도록합시다.

```py
urlpatterns = [
    path('sql/table', sql.views.table, name="table"),
    path('sql/read', sql.views.select, name="select"),
    path('sql/insert', sql.views.insert, name="insert"),
    path('sql/update', sql.views.update, name="update"),
    path('sql/delete', sql.views.delete, name="delete")
]

```

- 이제 해당 코드들을 돌려보면서 이제 데이터들을 확인해보면 `Django`에서 `sql`을 돌려보았습니다.

## ORM

- `ORM`이라는 이름의 `APP`을 만들어보도록 하겠습니다.

```console
# django App create
python ./manage.py startapp orm
```

- `setting.py`에 `INSTALLED_APPS`에 `APP(orm)`이름을 추가해보록 하겠습니다.

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework', # Rest FrameWork
    'Calculator', # App Name Calculator
    'sql', # App Name Calculator
    'orm', # App Name Calculator
]
```

- `orm`이란 객체와 관계형 데이터베이스의 데이터를 자동으로 매핑(연결)해주는 것을 의미하는데요.

- `orm`의 장점은 `DB`와 `Backend`에 의존성을 줄일수 있게 해줍니다.

- 그럼 `models.py`는 어떤것일까요?

- `django`는 `models.py` 파일을 통해 데이터베이스를 조작합니다.

- 각 app에는 models.py라고 하는 파일이 있으며 ORM이란 이름에서 유추할 수 있듯이 우리는 class를 이용하여 데이터베이스에 들어갈 객체를 설계하고 데이터베이스와 매핑한다.

- `models.py`에서 필드를 지정하ㅓ 각각의 클래스 변수는 `models.CharField()`, `models,IntegerField()`, `models.DateTimeField()`, `models.TextField()` 등의 각 필드 타입에 맞는 Field 클래스 객체를 생성하여 할당합니다.

<p align="center"><img src="./IMG/8.png "></p>

- Django 데이터 필드 타입

```py
models.BinaryField() : Binary - Blob field로 binary 데이터를 저장한다

models.BooleanField() : Boolean - Boolean field로 True/Flase(or 1/0) 값을 저장한다.

models.NullBooleanField() : Boolean - Boolean field와 같지만 null 값을 허용한다.

models.DateField() : Date/time - date field로 date를 저장한다.

models.TimeField() : Date/time - time field로 time을 저장한다.

models.DateTimeField() : Date/time - datetime field로 date와 time을 저장한다.

models.DurationField() : Date/time - 기간을 저장하는 필드

models.AutoField() : Number - 자동으로 값이 커지는 정수를 생성하는 필드

models.BigIntegerField() : Number

models.DecimalField(decimal_places=X, max_digits=Y) : Number - 숫자가 maximum X digit 과 Y decimal point를 갖게하며 X 와 Y 값은 필수이다.

models.FloatField() : Number - float형의 숫자를 저장한다.

models.IntegerField() : Number - 정수를 저장한다.

models.PositiveIntegerField() : Number - Integer field와 같지만 양수만 갖도록 제한한다.

models.PositiveSmallIntegerField() : Number

options.SmallIntegerField() : Number

models.CharField(max_length=N) : Text - max_length 값을 필수로 같는 character field

models.TextField() : Text

models.EmailField() : Text - django의 EmailValidator로 text가 email로 유효한지 판단할 수 있게 한다.

models.FileField() : Text

models.FilePathField() : Text

models.ImageField() : Text

models.GenericIPAddressField() : Text - 유효한 IPv4 나 IPv6 address만 받아들인다.

models.SlugField() : Text

models.URLField() : Text

models.UUIDField() : Text

```

- `orm`을 통해 `Django`에서 코드를 만들고 이를 `DB(mysql)`에 연결하여 `Backend`에서 컨트롤 하기 쉽게 만들어 보도록 하겠습니다.

```py
from django.db import models

# 설명만을 위한 모델로, 상당히 대충 작성 되었습니다:)
class Article(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to="uploads"
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.titl
```

- 이제 `orm/moodels.py`에 있는 코드를 `DB`에 반영 해 `Artcle`이라는 테이블을 만들도록 하겠습니다.

```console
python manage.py makemigrations

python manage.py migrate
```

- `makemigrations`을 실행하면 모델을 변경시킨 사실 또는 새로 생성한 모델들과 같은 변경사항을 migrations로 저장하고자 Django에게 알려줍니다.

- `migration`은 Django가 모델의 변경사항을 저장하는 방법입니다.

- 여기서 `mysql`을 켜서 해당 `table`이 있는지 확인해 보면 아래와 같이 나오게 될것입니다.

<p align="center"><img src="./IMG/2.png "></p>

- 그럼 여기서 매번 이렇게 `workbench`를 사용해야하나요? 라는 궁금증이 생길수도 있는데, `django`에서는ㄴ `admin`페이지를 통해 확인을 해볼수 있습니다.

```console
python manage.py createsuperuser
```

- 해당 명령어를 타이핑 하시고 아이디와 비밀번호를 설정하시면 됩니다.

- 그럼 `orm/admin.py`에서 `orm/models.py`에서 작성한 테이블을 연결 시켜주도록 하겠습니다.

```py
from django.contrib import admin
from .models import Article

admin.site.register(Article)
```

- 이제 서버를 실행시키고 `127.0.0.1/admin`에 들어가보면 아래와 같이 나올겁니다.

<p align="center"><img src="./IMG/3.png "></p>

- `createsuperuser`에서 작성한 ID,PW를 타이핑 하시고 들어가보면 아래와 같이 나옵니다.

<p align="center"><img src="./IMG/4.png "></p>

- 여기서 `omr`쪽을 보시면 `Artcle`테이블이 있는것을 확인해볼수있습니다.

<p align="center"><img src="./IMG/5.png "></p>

## Serialize

- 이제 `Serialize`에 대해 배워볼 시간입니다.

- `Serialzie`는 `쿼리셋,모델 인스턴스 등의 complex type(복잡한 데이터)를 JSON, XML등의 컨텐트 타입으로 쉽게 변환 가능한 python datatype으로 변환시켜주는 친구입니다.

- `model`에 담겨있는 데이터를 `Client`에서 원하는 데이터 타입으로 보내주거나 반대로 `Client`가 받아오는 데이터를 활요하는데 유용합니다.

- `orm`폴더에서 `serializers.py`라는 파일을 만들고 아래와 같이 타이핑 해주시면 `Serialize`가 완성됩니다.

```py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()

    def create(self, validated_data):

        # Create and return a new `Article` instance, given the validated data.
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        #Update and return an existing `Article` instance, given the validated data.
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance
```

- `serializer` 클래스의 첫 번째 부분은 직렬화되는 필드를 정의합니다.

- `create()` 및 `update()`는 호출 할 때 데이터를 만들거나 수정하는 방법에 대한 정의를 해주는곳입니다.

- 그럼 `serializer`가 작동이 잘 되었는지 확인해보록 하겠습니다.

- `python manage.py shell`를 쳐주시고 아래 코드를 하나씩 차근 차근 넣어 보겠습니다.

```py
from orm.models import Article

from orm.serializers import ArticleSerializer

from rest_framework.renderers import JSONRenderer

from rest_framework.parsers import JSONParser

a = Article(title = 'New Article', author ='Parwiz', email = 'par@gmail.com', )

a.save()

serializer = ArticleSerializer(a)

serializer.data

content = JSONRenderer().render(serializer.data)

serializer = ArticleSerializer(Article.objects.all(), many=True)

serializer.data

```

- 결과물을 통해 `serialize`가 작동하는것을 확인해 볼수있었습니다.

- 하지만 테이블 마다 이러한 절차를 거치게 된다면 많이 불편하다고 생각이 들수 있습니다.

- 그래서 `Django rest Framework`에서는 이러한 `model`에 대한 `serialize`를 함수를 제공하고 있습니다.

- 다시 `orm/serialziers.py`로 가셔서 코드를 `모두 주석`처리를 하시고 밑에 코드를 넣어주시면 됩니다.

```py
# orm/serialziers.py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True
    class Meta:
        model = Article
        fields = '__all__'
```

- 코드가 상당히 짧아 졌다는걸 알수있습니다.

- 자 이제 `REST API`를 통해 모델을 출력해보도록 하겠습니다.

- `orm/views.py`에서 아래 코드를 작성해 `Rest_Framework`를 사용하기 전에는 어떻게 출력을 했는지 보여드리겠습니다.

```py
#orm/views.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer

@csrf_exempt
def article_list(request):
    if request.method == 'GET': #GET 방식 통신일때
        articles = Article.objects.all () # Article 테이블의 모든 자료를 받아옴
        serializer = ArticleSerializer(articles, many=True) # Serializer를 통해 직렬화 게시
        return JsonResponse(serializer.data, safe=False) # JSON 타입으로 응답!

    elif request.method == 'POST': #Post 방식일때
        data = JSONParser().parse(request) # JSON형태로 들어오는 데이터를 분해
        serializer = ArticleSerializer(data=data)# 직렬화 게시
        if serializer.is_valid(): #들어온 데이터 타입이 테이블에 적절한지 타입 비교
            serializer.save() # 적절하다면 테이블에 저장합니다
            return JsonResponse(serializer.data, status=201)  # JSON 타입으로 응답!
        return JsonResponse(serializer.errors, status=400)  # JSON 타입으로 응답!

```

- 이제 `urls.py`에서 `URL`에 대한 설정을 해주도록 하겠습니다.

```py
from django.contrib import admin
from django.urls import path
from orm.views import article_list,article_detail,ArticleAPIView,ArticleDetails
import Calculator.views
import sql.views

urlpatterns = [
    path('admin/', admin.site.urls),

    #sql
    path('sql/table', sql.views.table, name="table"),
    path('sql/read', sql.views.select, name="select"),
    path('sql/insert', sql.views.insert, name="insert"),
    path('sql/update', sql.views.update, name="update"),
    path('sql/delete', sql.views.delete, name="delete"),

    # FBV
    path('add/', Calculator.views.fun_calc_add),
    path('sub/', Calculator.views.fun_calc_sub),
    path('mul/', Calculator.views.fun_calc_mul),
    path('div/', Calculator.views.fun_calc_div),

    # CBV
    path('cls_add/', Calculator.views.class_add.as_view()),
    path('cls_sub/', Calculator.views.class_sub.as_view()),
    path('cls_mul/', Calculator.views.class_mul.as_view()),
    path('cls_div/', Calculator.views.class_div.as_view()),

    # ORM
    path('article/', article_list),
]
```

- 이렇게 하시고 `vsocde extension thunder-client`에서 아래와 같이 타이핑을 쳐보도록 하겠습니다.

<p align="center"><img src="./IMG/6.png "></p>

- 그러면 테이블에 있는 값을 나타내 주는것을 볼수있습니다.

- 하지만 우리는 `REST Framework`에 대해 공부를 하기 때문에 이를 수정해 보도록 하겠습니다.

```py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
        # return JsonResponse(serializer.data, safe=False) #이전에 사용하는 방식

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # return JsonResponse(serializer.data, status=201)  #이전에 사용하는 방식
        # return JsonResponse(serializer.errors, status=400)   #이전에 사용하는 방식
```

- 그럼 `JSON` 타입에 대해 정의를 하지 않고 사용할수 있게 되고 `api_view`를 사용할수 있게 됩니다.

- 마지막으로 `article`을 좀더 상세히 볼수 있는 `API`를 구축하고 마치도록 하겠습니다.

```py

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk) # 몇번째 게시물인지 체크!
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        # return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
        # return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # return JsonResponse(serializer.data)
        # return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # return HttpResponse(status=204)
```

- 또한 `urls.py`에서도 이를 수정해야 할것입니다.

```py
from django.contrib import admin
from django.urls import path
from orm.views import article_list,article_detail,ArticleAPIView,ArticleDetails
import Calculator.views
import sql.views

urlpatterns = [
    path('admin/', admin.site.urls),

    #sql
    path('sql/table', sql.views.table, name="table"),
    path('sql/read', sql.views.select, name="select"),
    path('sql/insert', sql.views.insert, name="insert"),
    path('sql/update', sql.views.update, name="update"),
    path('sql/delete', sql.views.delete, name="delete"),

    # FBV
    path('add/', Calculator.views.fun_calc_add),
    path('sub/', Calculator.views.fun_calc_sub),
    path('mul/', Calculator.views.fun_calc_mul),
    path('div/', Calculator.views.fun_calc_div),

    # CBV
    path('cls_add/', Calculator.views.class_add.as_view()),
    path('cls_sub/', Calculator.views.class_sub.as_view()),
    path('cls_mul/', Calculator.views.class_mul.as_view()),
    path('cls_div/', Calculator.views.class_div.as_view()),

    # ORM
    path('article/', article_list),
    path('detail/<int:pk>/', article_detail),


]
```

- 이렇게 하면 `127.0.0.1/detail/1` 치게되면 `article`의 첫번째 자료를 받아 오게 되는것입니다.

<p align="center"><img src="./IMG/7.png "></p>
