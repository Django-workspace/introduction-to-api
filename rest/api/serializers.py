from rest_framework import serializers
from api.models import TestModel
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model=TestModel
        fields=['id','name']