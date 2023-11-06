from django.urls import path
from .views import *


urlpatterns = [
    path("accounts/register/",Register.as_view()),
    path("accounts/profile/<int:pk>/view/",Profile.as_view()),
    path("accounts/profile/<int:pk>/edit/",edit_),
    path("accounts/login/",login_)
]

