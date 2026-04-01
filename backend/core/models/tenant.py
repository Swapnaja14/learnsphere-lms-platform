from django.db import models
from .base import BaseModel

class Tenant(BaseModel):
    name = models.CharField(max_length=255)
    subscription_plan = models.CharField(max_length=100)
    status = models.CharField(max_length=50)


class Client(BaseModel):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Branch(BaseModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Site(BaseModel):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)