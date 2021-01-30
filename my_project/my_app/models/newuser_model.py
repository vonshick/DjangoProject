from django.db import models
from django.contrib.auth.models import User


class NewUser(User):
    date_of_birth = models.DateField()
