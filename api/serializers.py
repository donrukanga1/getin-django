from rest_framework import serializers
from backend.models import *
from datetime import date


class ListSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField('get_girls_age')

    def get_girls_age(self, girl):
        today = date.today()
        age = today.year - girl.date_of_birth.year
        return age

    class Meta:
        model = PregnantGirl
        fields = ('id', 'name', 'age', 'marital_status', 'education_level')


class RegisterGirlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PregnantGirl
        fields = ('name', 'marital_status', 'education_level', 'date_of_birth')