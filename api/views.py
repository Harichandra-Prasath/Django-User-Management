from rest_framework.decorators import api_view
from rest_framework import generics
from .models import User
from .serializers import *
from .exceptions import *
from firebase_admin import auth
from django.http import JsonResponse,QueryDict,HttpResponseRedirect
# Create your views here.

class Register(generics.CreateAPIView):   
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class Profile(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer

@api_view(["PUT"])
def edit_(request,pk):
    put = QueryDict(request.body)
    username = put.get('username')
    first_name = put.get('first_name')
    last_name = put.get('last_name')


    if username=="":
            raise UsernameEmpty
    if len(User.objects.filter(username=username))==1:
            return JsonResponse({"error":f"User already exist with the username {username}"},status=400)
    if len(username)>100 or len(first_name)>100 or len(last_name)>100:
            raise MaxlengthViolation
    try:
         user = User.objects.get(pk=pk)
    except:
         raise UserDoesnotExist
    user.username = username
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    return JsonResponse({"username":user.username,"email":user.email,"full_name":user.get_full_name()})


@api_view(["POST"])
def login_(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user=User.objects.get(username=username)
    except:
        raise InvalidCredentials
    if not user.check_password(password):
        raise InvalidCredentials
    custom_token = auth.create_custom_token(str(user.pk)).decode('utf-8')
    return JsonResponse({"email":user.email,"username":user.username,"custom_token":custom_token})


