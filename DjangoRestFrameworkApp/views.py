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
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import (
      IsAuthenticated,
      IsAdminUser,
      AllowAny,
      IsAuthenticatedOrReadOnly,
      DjangoModelPermissions,
      DjangoModelPermissionsOrAnonReadOnly
)


class EmployeeCRUD(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]



'''

suppose there are 10 model views are there, and all of them want the token authenticatoin except 9th one.
Here, to apply the authentication for all model views we have to se authentication globally and
for 9th one who don't want the authentication we have to override the by the follwoing two lines

===>>>    permission_classes = [AllowAny]  <<<====

'''
