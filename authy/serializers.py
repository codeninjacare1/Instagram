from rest_framework import serializers
from .models import *



class ProfileSerializer(serializers.ModelSerializer):
    following = serializers.PrimaryKeyRelatedField(many=True, queryset=Profile.objects.all())
    blocked_users = serializers.PrimaryKeyRelatedField(many=True, queryset=Profile.objects.all())
    class Meta:
        model = Profile
        fields = '__all__' 