from django.db import models
from .base import BaseModel
from .tenant import Client, Branch, Site

class User(BaseModel):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)


class Role(BaseModel):
    name = models.CharField(max_length=100, unique=True)


class Permission(BaseModel):
    name = models.CharField(max_length=255)


class UserRole(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


class RolePermission(BaseModel):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)