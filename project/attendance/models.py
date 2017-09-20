# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from project.api.models import *

# Create your models here.


class Attendance(models.Model):
    student = models.ForeignKey(CustomUser)
    date_taken = models.DateTimeField(auto_now=True)
    is_present = models.BooleanField(default=False)
    class_teacher = models.ForeignKey(CustomUser)#change profiles
