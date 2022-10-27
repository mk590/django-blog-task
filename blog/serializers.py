from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import *

class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog 
        fields='__all__'
        
class tagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tags
        fields='__all__'
        
        
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        