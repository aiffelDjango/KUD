from rest_framework import serializers
from .models import imagePost 

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = imagePost
        fields = '__all__'
