"""RestAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    
    # CLS ORM
    path('cls_article/', ArticleAPIView.as_view()),
    path('cls_detail/<int:id>/', ArticleDetails.as_view()),

]

