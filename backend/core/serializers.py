from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Prompt
from .models import Project

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']


class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ['id', 'title', 'content', 'created_at']
        read_only_fields = ['id', 'created_at']


class ChatInputSerializer(serializers.Serializer):
    message = serializers.CharField()
