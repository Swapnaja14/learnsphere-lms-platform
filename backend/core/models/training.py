from django.db import models
from .base import BaseModel
from .courses import Course
from .users import User

class TrainingSession(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    trainer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    training_date = models.DateField()
    start_time = models.TimeField()
    duration_minutes = models.IntegerField()

    location = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, default="scheduled")


class TrainingAttendance(BaseModel):
    session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    attendance_status = models.CharField(max_length=50)
    check_in_time = models.DateTimeField(null=True, blank=True)
    check_out_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('session', 'user')


class TrainingResult(BaseModel):
    session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    assessment = models.ForeignKey('Assessment', on_delete=models.SET_NULL, null=True)

    score = models.FloatField()
    total_marks = models.IntegerField()
    percentage = models.FloatField()

    completion_time_seconds = models.IntegerField(null=True, blank=True)
    submitted_at = models.DateTimeField()

    class Meta:
        unique_together = ('session', 'user')