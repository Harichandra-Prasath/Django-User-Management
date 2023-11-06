from .models import User
import jwt


from django.http import JsonResponse
from django.conf import settings

class FirebaseAuthenticationMiddleWare:
    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        excluded_endpoints = ['/api/accounts/register/','/api/accounts/login/']
        if request.path not in excluded_endpoints:
            if 'HTTP_AUTHORIZATION' in request.META:
                authorization_header = request.META['HTTP_AUTHORIZATION']
                _,id_token = authorization_header.split()
                try:
                    decoded_token = jwt.decode(id_token,verify=False,options={'verify_signature':False})
                    user = User.objects.get(pk=int(decoded_token["uid"])) 
                    print(user.username)
                except:
                    return JsonResponse({"error":"Invalid token"},status=401)
            else:
                return JsonResponse({"error":"Authorization Header Missing"},status=401)
        return self.get_response(request)