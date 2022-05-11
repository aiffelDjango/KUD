from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.

def sqlExcuter(sql):
    try:
        cursor = connection.cursor()
        result = cursor.execute(sql)
        datas = cursor.fetchall()

        if len(datas)<1 :
            cursor.execute("select * from tmp")
            datas = cursor.fetchall()

        connection.commit()
        connection.close()
        return datas
    except Exception as ex:
        connection.rollback()
        return ("Fail to sql, the string is" + sql + "error: " + str(ex))


def table(request):
    mysql = "CREATE TABLE tmp (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50),age INT);"
    result = sqlExcuter(mysql)
    return HttpResponse(result)

def select(request):
    mysql = "select * from tmp;"
    result = sqlExcuter(mysql)
    return HttpResponse(result)

def insert(request):
    mysql = " INSERT INTO tmp(ID, Name, age) VALUES(2, 'KUD2', '3'); "
    result = sqlExcuter(mysql)
    return HttpResponse(result)

def update(request):
    mysql = "UPDATE tmp SET age = 2002 WHERE id = 1;"
    result = sqlExcuter(mysql)
    return HttpResponse(result)

def delete(request):
    mysql = " DELETE FROM tmp WHERE Name = 1;"
    result = sqlExcuter(mysql)
    return HttpResponse(result)