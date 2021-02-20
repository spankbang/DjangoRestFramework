from django.shortcuts import render
from django.views.generic import View
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.mixins import *

from rest_framework.viewsets import ModelViewSet


class EmployeeCRUD(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
