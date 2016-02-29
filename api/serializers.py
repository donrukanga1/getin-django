from rest_framework import serializers
from rest_framework.authtoken.models import Token

from backend.models import *
from datetime import date

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=32)
    password = serializers.CharField(max_length=128)


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField('get_user_token')

    def get_user_token(self, user):
        token, created = Token.objects.get_or_create(user=user)
        return token.key


    class Meta:
        model = User
        fields = ('id', 'username','first_name', 'last_name', 'phone_number', 'type', 'token')


class PregnantGirlSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField('get_girls_age')

    def get_girls_age(self, girl):
        today = date.today()
        age = today.year - girl.date_of_birth.year
        return age

    class Meta:
        model = PregnantGirl
        fields = ('id', 'name', 'age', 'marital_status', 'education_level', 'emergency_contact', 'contact_type', 'contact_number', 'number_of_children', 'has_gone_for_anc',
                  'prefered_language', 'village', 'parish', 'subcounty', 'latitude', 'longitude')


class RegisterGirlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PregnantGirl
        fields = ('name', 'marital_status', 'education_level', 'date_of_birth', 'emergency_contact', 'contact_type', 'contact_number', 'number_of_children', 'has_gone_for_anc',
                  'prefered_language', 'village', 'parish', 'subcounty', 'latitude', 'longitude')


class VHTSerializer(serializers.ModelSerializer):
    mapped_girls = serializers.SerializerMethodField('get_girls_mapped_by_vht')

    def get_girls_mapped_by_vht(self, vht):
        girls = PregnantGirl.objects.filter(mapped_by=vht)
        serializer = PregnantGirlSerializer(instance=girls, many=True)
        return serializer.data


    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'mapped_girls')


class AppointmentSerializer(serializers.ModelSerializer):
    girl = PregnantGirlSerializer()
    class Meta:
        model = AntenatalVist
        fields = '__all__'