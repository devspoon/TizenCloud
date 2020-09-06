from rest_framework import serializers
from .models import AIAnalysis

class AIASerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = AIAnalysis
        fields = ('id','email','image','age','resultage','compareyesterday','skincolor','register_date','register_date')
