from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Diseases
from rest_framework.authtoken.models import Token
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=['url','id','username','password']
    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        token=Token.objects.create(user=user)
        return user
class DiseaseSerialzer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Diseases
        fields=['url','id','title']