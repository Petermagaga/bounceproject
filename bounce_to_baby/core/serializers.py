
from django.contrib.auth import get_user_model

from rest_framework import serializers
from .models import User,JournalEntry,FAQ

User=get_user_model()

class UserSerializer(serializers.ModelSerializer):
    due_date= serializers.ReadOnlyField()
    trimester=serializers.ReadOnlyField()
    profile_picture=serializers.ImageField(required=False)

    class Meta:
        model=User
        fields=['id','username','email','age','location','pregnacy_start_date','due_date','trimester','profile_picture']

class registerSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['username','email','password']

    def create(self,validated_data):
        user=User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class PregnancyInfoSerializer(serializers.Serializer):
    current_week =serializers.IntegerField()
    trimester=serializers.CharField()
    due_date=serializers.DateField()
    baby_size=serializers.CharField()
    weekly_tip= serializers.CharField()
    nutrition_advice =serializers.CharField()


class journalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model=JournalEntry
        fields=['id','mood','symptoms','note','created_at']


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model=FAQ
        fields=['id','question','answer','topic']
