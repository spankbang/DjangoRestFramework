from django.shortcuts import render
from django.views.generic import View
from .models import Employee
from .serializers import EmployeeSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated


class EmployeeCRUD(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]


'''
JWT_AUTH = {

        'JWT_ENCODE_HANDLER':                   'rest_framework_jwt.utils.jwt_encode_handler',
        'JWT_DECODE_HANDLER':                   'rest_framework_jwt.utils.jwt_decode_handler',
        'JWT_PAYLOAD_HANDLER':                  'rest_framework_jwt.utils.jwt_payload_handler',
        'JWT_PAYLOAD_GET_USER_ID_HANDLER':      'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
        'JWT_RESPONSE_PAYLOAD_HANDLER':         'rest_framework_jwt.utils.jwt_response_payload_handler',
        'JWT_SECRET_KEY':                        settings.SECRET_KEY,
        'JWT_GET_USER_SECRET_KEY':               None,
        'JWT_PUBLIC_KEY':                        None,
        'JWT_PRIVATE_KEY':                       None,
        'JWT_ALGORITHM':                        'HS256',
        'JWT_VERIFY':                            True,
        'JWT_VERIFY_EXPIRATION':                 True,
        'JWT_LEEWAY':                            0,
        'JWT_EXPIRATION_DELTA':                  datetime.timedelta(seconds=300),
        'JWT_AUDIENCE':                          None,
        'JWT_ISSUER':                            None,
        'JWT_ALLOW_REFRESH':                     False,
        'JWT_REFRESH_EXPIRATION_DELTA':          datetime.timedelta(days=7),
        'JWT_AUTH_HEADER_PREFIX':               'JWT',
        'JWT_AUTH_COOKIE':                       None,
        
}
'''
