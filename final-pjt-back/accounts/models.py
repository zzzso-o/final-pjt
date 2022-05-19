from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import IntegerField

class User(AbstractUser):
    user_grade = IntegerField()