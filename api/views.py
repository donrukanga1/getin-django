from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView, get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.models import *
from api.serializers import *

class RegisterPregnantGirl(CreateAPIView):
    model = PregnantGirl
    serializer_class = RegisterGirlsSerializer

class ListPregnantGirls(ListAPIView):
    model = PregnantGirl
    serializer_class = ListSerializer
    paginate_by = 20

    def get_queryset(self):
        girls = PregnantGirl.objects.all()
        return girls