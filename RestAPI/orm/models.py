from django.db import models

# Create your models here.

# 설명만을 위한 모델로, 상당히 대충 작성 되었습니다:)
class Article(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to="uploads")
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title