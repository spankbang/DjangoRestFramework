from django.shortcuts import render
from django.views.generic import View
from .models import Employee
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import EmployeeSerializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt,name="dispatch")
class EmployeeCRUD(View):

    def get(self, requests,*args,**kwargs):
        json_data = requests.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get('id', None)
        if id is not None:
            emp = Employee.objects.get(id=id)
            emp_serializer = EmployeeSerializers(emp)
            json_data = JSONRenderer().render(emp_serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        emp = Employee.objects.all()
        emp_serializer = EmployeeSerializers(emp,many=True)
        json_data = JSONRenderer().render(emp_serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, requests, *args, **kwargs):
        json_data = requests.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        serialized_data = EmployeeSerializers(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            msg = "Resource added successfully."
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")
        json_data = JSONRenderer().render(serialized_data.errors)
        return HttpResponse(json_data, content_type="application/json")


    def put(self, requests, *args, **kwargs):
        json_data = requests.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get("id")
        emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializers(emp, data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = "Resource updated successfully."
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")

    def delete(self, requests, *args, **kwargs):
        json_data = requests.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get("id")
        emp = Employee.objects.get(id=id)
        emp.delete()
        json_data = "Deleted successfully"
        return HttpResponse(json_data, content_type="application/json")
