from django.shortcuts import render
from django.views.generic import View
from .models import Employee
from .serializers import EmployeeSerializer


from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from .permissions import IsReadOnly, IsGETorPATCH, SunnyLeonePermission


class EmployeeCRUD(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication]

    ######## please check the permissions.py file for following ########
    
    permission_classes = [SunnyLeonePermission]
    # permission_classes = [IsReadOnly]
    # permission_classes = [IsGETorPATCH]
