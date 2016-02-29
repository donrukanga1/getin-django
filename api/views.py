from django.contrib.auth import authenticate
from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView, get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.models import *
from api.serializers import *


class Login(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']
            user = authenticate(username=username, password=password)

            print user

            if user:
                if user.is_active:
                    token, created = Token.objects.get_or_create(user=user)
                    serializer = UserSerializer(instance=user)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    content = {'detail': 'User not activated'}
                    return Response(content, status=status.HTTP_401_UNAUTHORIZED)
            else:
                content = {'detail': 'Unable to login with provided credentials.'}
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class RegisterPregnantGirl(CreateAPIView):
    model = PregnantGirl
    serializer_class = RegisterGirlsSerializer

class ListPregnantGirls(ListAPIView):
    model = PregnantGirl
    serializer_class = PregnantGirlSerializer
    paginate_by = 20

    def get_queryset(self):
        girls = PregnantGirl.objects.all()
        return girls

class VHTList(ListAPIView):
    model = User
    serializer_class = VHTSerializer
    paginate_by = 20

    def get_queryset(self):
        vhts = User.objects.filter(type='vht')
        return vhts

class UpcomingAppointments(ListAPIView):
    model = AntenatalVist
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        today = datetime.datetime.today()
        upcoming_appointments = AntenatalVist.objects.filter(Q(date__gte=today))
        return upcoming_appointments

class MissedAppointments(ListAPIView):
    model = AntenatalVist
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        today = datetime.datetime.today()
        missed_appointments = AntenatalVist.objects.filter(Q(date__gte=today))
        return missed_appointments

class Search(ListAPIView):
   serializer_class = PregnantGirlSerializer

   def get_queryset(self):
      query = self.request.query_params.get('query', None)
      girls = PregnantGirl.objects.filter(name__icontains=query)

      return girls