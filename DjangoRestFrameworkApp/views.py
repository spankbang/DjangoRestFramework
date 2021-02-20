from django.shortcuts import render
from django.views.generic import View
from .models import Employee
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from .serializers import NameSerializer

from rest_framework import viewsets


class TestViewSet(viewsets.ViewSet):
    def list(self, request):
        colors = ['red', 'green', 'blue']
        return Response({"msg": "Happy new year", "colors": colors})

    def create(self, request):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get("name")
            msg = f"Hello, {name}, and fuck you 2021 !"
            return Response({"msg": msg})
        else:
            return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        return Response({"msg": "This is retieve method !"})

    def update(self, request, pk=None):
        return Response({"msg": "This is update method !"})

    def partial_update(self, request, pk=None):
        return Response({"msg": "This is partial_update method !"})

    def destroy(self, request, pk=None):
        return Response({"msg": "This is destroy method !"})
