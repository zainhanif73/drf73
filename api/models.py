from pyexpat import model
from django.db import models

class Admin(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class city(models.Model):
    name = models.CharField(max_length=200)


class major(models.Model):
    name = models.CharField(max_length=300)


