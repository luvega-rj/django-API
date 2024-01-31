from rest_framework import serializers
from .models import Jifunze

class JifunzeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jifunze
        fields = ['id','name','description']