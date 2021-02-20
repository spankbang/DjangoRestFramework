from django.shortcuts import render
from django.views.generic import View
from .models import Employee
from .serializers import EmployeeSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import *


class EmployeeAPIView(APIView):

    def get(self, request, format=None):
        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs, many=True)
        return Response(serializer.data)

# Only list the records
class EmployeeListApiView(ListAPIView):
    # queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        qs = Employee.objects.all()
        name = self.request.GET.get("ename")
        if name is not None:
            qs = qs.filter(ename__icontains=name)
        return qs

# only create
class EmployeeCreateApiView(CreateAPIView):
    qs = Employee.objects.all()
    serializer_class = EmployeeSerializer

# only retieve
class EmployeeRetrieveApiView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# only update
class EmployeeUpdateApiView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# only delete
class EmployeeDeleteApiView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer




# list employee records and also create it
class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# list employee records and also update it
class EmployeeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# list employee records and also delete it
class EmployeeRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# list employee records and also update and delete it
class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


######################################################  only two end points  ######################################################

class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
