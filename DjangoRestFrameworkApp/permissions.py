from rest_framework.permissions import BasePermission, SAFE_METHODS



'''
Define our own Permission class which allows only SAFE_METHODS
(GET,HEAD,OPTIONS)
'''
class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False

'''
Defining our own permission class which allows only GET and PATCH methods
'''
class IsGETorPATCH(BasePermission):
    def has_permission(self, request, view):
        safe_list = ['GET','PATCH']
        if request.method in safe_list:
            return True
        else:
            return False


'''
Define our own Permission class if the name is sunny then allow all methods
If the name is not sunny and the name contains even number of characters then allow
only safe methods otherwise not allowed to perform any operation

'''
class SunnyLeonePermission(BasePermission):
    def has_permission(self, request, view):
        username = request.user.username
        if username.lower() == "sunny":
            print(username)
            return True
        elif username.lower != "sunny" and len(username) % 2 == 0 and request.method in SAFE_METHODS:
            return True
        else:
            return False
