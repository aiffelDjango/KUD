from rest_framework import serializers
from .models import imagePost


class PostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = imagePost
        fields = "__all__"
