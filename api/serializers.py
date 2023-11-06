from rest_framework import serializers
from .models import User
from .exceptions import *
from django.http import HttpResponseRedirect

class RegisterSerializer(serializers.ModelSerializer):  
    email = serializers.EmailField(allow_blank=True)      # For custom exceptions ,we are making required to
    username = serializers.CharField(allow_blank=True)
    password = serializers.CharField(allow_blank=True,write_only=True)
    first_name = serializers.CharField(allow_blank=True,write_only=True)
    last_name = serializers.CharField(allow_blank=True,write_only=True)
    class Meta:
        model = User
        fields = ["email","username","password","first_name","last_name"]
    
    def validate(self, data):

        if data['email'] ==""or data['username'] =="" or data['password'] =="":
            raise RequriedVioaltion
        
        email = data['email']
        username= data['username']
        password = data['password']


        if len(User.objects.filter(username=username))==1:
            raise UsernameAlreadyExists
        if len(password)<8:
            raise BadPassword
        if len(username)>100 or len(data['first_name'])>100 or len(data['last_name'])>100:
            raise MaxlengthViolation
        
        return data

    def create(self,validated_data):
        email = validated_data['email']
        username= validated_data['username']
        password = validated_data['password']

        user = User(email=email,username=username,first_name=validated_data["first_name"],last_name=validated_data["last_name"])
        user.set_password(password)
        user.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField('get_full_name')
    class Meta:
        model = User
        fields = ['username','email','full_name']
    
    def get_full_name(self,obj):
        return f"{obj.first_name} {obj.last_name}"

        