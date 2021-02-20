"""DjangoRestFrameworkProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from DjangoRestFrameworkApp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-rest/", include("rest_framework.urls")),
    path("api/", EmployeeAPIView.as_view()),
    path("list_api_view/", EmployeeListApiView.as_view()),
    path("create_api_view/", EmployeeCreateApiView.as_view()),
    path("retrieve_api_view/<int:pk>/", EmployeeRetrieveApiView.as_view()),
    path("update_api_view/<int:pk>/", EmployeeUpdateApiView.as_view()),
    path("delete_api_view/<int:pk>/", EmployeeDeleteApiView.as_view()),

    # multiple at a same time
    path("list_create_api_view/", EmployeeListCreateAPIView.as_view()),
    path("retrieve_update_api_view/<int:pk>/", EmployeeRetrieveUpdateAPIView.as_view()),
    path("retrieve_delete_api_view/<int:pk>/", EmployeeRetrieveDestroyAPIView.as_view()),
    path("retrieve_update_delete_api_view/<int:pk>/", EmployeeRetrieveUpdateDestroyAPIView.as_view()),


    ##########  only two end points  #############
    path("only_two_end_points_retrieve_create_update_delete/", EmployeeListCreateAPIView.as_view()),
    path("only_two_end_points_retrieve_create_update_delete/<int:pk>/", EmployeeRetrieveUpdateDestroyAPIView.as_view()),



]
