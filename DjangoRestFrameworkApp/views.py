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
from rest_framework.mixins import *

class EmployeeListCreateModelMixin(CreateModelMixin, ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EmployeeRetrieveUpdateDeleteModelMixin(UpdateModelMixin,DestroyModelMixin,RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
