# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Session(models.Model):
    school_session = models.CharField(max_length=9, default='2017/2018')
    session_active = models.NullBooleanField(default=False)

    def __str__(self):
        return str(self.school_session)


class Term(models.Model):
    term_options = (
        (1, '1st Term'),
        (2, '2nd Term'),
        (3, '3rd Term')
    )
    term = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.term)


class School(models.Model):
    name = models.CharField(max_length=256, default='')

    def __str__(self):
        return str(self.name)


class Class(models.Model):
    name = models.CharField(max_length=256, null=True)
    school = models.ForeignKey(School)

    def __str__(self):
        return str(self.name)


class Subject(models.Model):
    options = (
        ('C', 'Compulsory'),
        ('E', 'Elective')
    )
    name = models.CharField(max_length=256, default='')
    subject_type = models.CharField(max_length=1, choices=options, default='')
    ca_score = models.IntegerField(null=True, blank=True)
    exam_score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class CustomUser(AbstractUser):
    type_choices = (
        (1, 'Admin'),
        (2, 'Principal'),
        (3, 'Teacher'),
        (4, 'Parent'),
        (5, 'Student'),
    )
    sex_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    type = models.IntegerField(null=True, blank=True)
    sex = models.CharField(max_length=10, choices=sex_choices, help_text='Gender Option')
    d_o_b = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    tel = models.CharField(max_length=14, null=True, blank=True)
    nationality = models.CharField(max_length=20, null=True, blank=True)
    state_of_origin = models.CharField(max_length=20, null=True, blank=True)
    lga = models.CharField(max_length=20, null=True, blank=True)
    religion = models.CharField(max_length=20, null=True, blank=True)
    school = models.ForeignKey(School, null=True, blank=True)
    class_room = models.ForeignKey(Class, null=True, blank=True)
    subject = models.ForeignKey(Subject, null=True, blank=True)

    def __str__(self):
        return str(self.last_name) + ", " + str(self.first_name)