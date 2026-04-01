from django.db import models
from .base import BaseModel
from .courses import Course
from .users import User

class Assessment(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Question(BaseModel):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)


class Option(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)


class Submission(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)