from rest_framework import serializers
from .models import Authentication

class AuthSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Authentication
        fields = ('id','email','image','result','register_date')
