from django.contrib import admin
from django.urls import include,path
import Landing.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('Landing/',include('Landing.urls')),
    path('',Landing.views.index,name="index"),
    path('study',Landing.views.study,name="index")
    # path('',Landing.views.index,name="index"),
]
