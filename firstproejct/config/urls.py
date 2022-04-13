from django.contrib import admin
from django.urls import include,path
import Landing.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('Landing/',include('Landing.urls')),
    path('landing',Landing.views.index,name="index")
    # path('',Landing.views.index,name="index"),
]
