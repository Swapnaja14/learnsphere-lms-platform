from django.db import models
from .base import BaseModel
from .users import User

class File(BaseModel):
    file_name = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Content(BaseModel):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)


class Tag(BaseModel):
    name = models.CharField(max_length=100)


class ContentTag(BaseModel):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)