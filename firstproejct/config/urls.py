from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static
import Landing.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Landing.views.index,name="index"),
    path('study',Landing.views.study,name="study"),
    path('sticker',Landing.views.sticker,name="sticker"),
    path('stickerResult',Landing.views.stickerResult,name="stickerResult")
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
