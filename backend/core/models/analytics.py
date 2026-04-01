from django.db import models
from .base import BaseModel
from .users import User

class Report(BaseModel):
    report_type = models.CharField(max_length=100)

    generated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    date_from = models.DateField()
    date_to = models.DateField()

    export_format = models.CharField(max_length=20)
    status = models.CharField(max_length=50)

    file_url = models.TextField(null=True, blank=True)


class ScheduledReport(BaseModel):
    report_type = models.CharField(max_length=100)

    frequency = models.CharField(max_length=50)
    recipient_emails = models.TextField()

    include_charts = models.BooleanField(default=True)
    password_protected = models.BooleanField(default=False)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    next_run = models.DateTimeField()


class ActivityLog(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    activity_type = models.CharField(max_length=100)
    description = models.TextField()

    ip_address = models.GenericIPAddressField(null=True, blank=True)
    device_info = models.TextField(null=True, blank=True)