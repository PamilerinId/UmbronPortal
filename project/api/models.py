# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    address = models.TextField(null=True, blank=True, unique= True)

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
        (4, 'Guardian'),
        (5, 'Student'),
    )
    sex_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    religion_choices = (
        ('Christianity', 'Christianity'),
        ('Islam', 'Islam'),
        ('Native Practice', 'Native Practice')
    )
    type = models.IntegerField(null=True, blank=True)
    sex = models.CharField(max_length=10, choices=sex_choices, help_text='Gender Option', null=True, blank=True)
    d_o_b = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    tel = models.CharField(max_length=14, null=True, blank=True)
    nationality = models.CharField(max_length=20, null=True, blank=True)#dropbox
    state_of_origin = models.CharField(max_length=20, null=True, blank=True)#dropdown
    lga = models.CharField(max_length=20, null=True, blank=True)#dropdown
    religion = models.CharField(max_length=20, choices=religion_choices, help_text='Religion Option', null=True, blank=True)

    def __str__(self):
        return str(self.last_name) + ", " + str(self.first_name)


class Principal(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    school_in_charge = models.ForeignKey(School, null=True, blank=True)

    def __str__(self):
        return str(self.user.last_name) + ", " + str(self.user.first_name)


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    school_employed = models.ForeignKey(School, null=True, blank=True)
    subject_s = models.ForeignKey(Subject, null=True, blank=True)
    is_classteacher = models.NullBooleanField(default=False)
    class_in_charge = models.ForeignKey(Class, null=True, blank=True)#handled in forms

    def __str__(self):
        return str(self.user.last_name) + ", " + str(self.user.first_name)


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    school_attending = models.ForeignKey(School, null=True, blank=True)
    classroom = models.ForeignKey(Class, null=True, blank=True)
    # guardian = models.ForeignKey(Guardian, null=True, blank=True)

    def __str__(self):
        return str(self.user.last_name) + ", " + str(self.user.first_name)


class Guardian(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    ward = models.ForeignKey(Student, null=True, blank=True)  # Parent and Student should be reverse accessed

    def __str__(self):
        return str(self.user.last_name) + ", " + str(self.user.first_name)


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if CustomUser.type == 2:
            Principal.objects.create(user=instance)
        if CustomUser.type == 3:
            Teacher.objects.create(user=instance)
        if CustomUser.type == 4:
            Guardian.objects.create(user=instance)
        if CustomUser.type == 5:
            Student.objects.create(user=instance)



@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if CustomUser.type == 2:
        instance.principal.save()
    if CustomUser.type == 3:
        instance.teacher.save()
    if CustomUser.type == 4:
        instance.guardian.save()
    if CustomUser.type == 5:
        instance.student.save()

