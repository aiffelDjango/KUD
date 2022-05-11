DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql', # 사용할 DBMS 
        'NAME' : 'KUD', # Mysql 데이터베이스 이름
        'USER' : 'root', # DB 접속 계정명
        'PASSWORD': '1q2w3e', # 해당 계정의 비밀번호
        'HOST' : '146.56.154.230', # IP
        'PORT' : '3306' # PORT
    }
}
SECRET_KEY = 'django-insecure-mcz1ug5qsx+=j((bm8n-^6+m76a=38ym+vgxtggvt5%ysck&)e'