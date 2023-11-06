from rest_framework.exceptions import APIException


class UsernameAlreadyExists(APIException):
    status_code = 400
    default_detail = "A user with that username already exists"
    default_code="user_already_exists"

class BadPassword(APIException):
    status_code = 400
    default_detail= "This password is too short. It must contain at least 8 characters"
    default_code="bad_password"

class RequriedVioaltion(APIException):
    status_code = 400
    default_detail = "Username,Email and password are required"
    default_code="required_violation"

class MaxlengthViolation(APIException):
    status_code = 400
    default_detail="Only 100 characters are allowed for a field"
    default_code="size_violation"


class UsernameEmpty(APIException):
    status_code = 400
    default_code="empty_username"
    default_detail="Updated Username cant be empty"

class InvalidCredentials(APIException):
    status_code = 400
    default_code = "Invalid"
    default_detail = "Username or password is invalid"

class UserDoesnotExist(APIException):
    status_code = 400
    default_code = "no_user"
    default_detail = "User doesnt exist"