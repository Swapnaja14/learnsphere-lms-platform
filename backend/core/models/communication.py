from django.db import models
from .base import BaseModel
from .users import User

class Group(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class GroupMember(BaseModel):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    role = models.CharField(max_length=50, default="member")
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('group', 'user')


class Message(BaseModel):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)

    message_text = models.TextField()
    attachment_url = models.TextField(null=True, blank=True)

    sent_at = models.DateTimeField(auto_now_add=True)


class Notification(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    message = models.TextField()

    type = models.CharField(max_length=50)
    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)