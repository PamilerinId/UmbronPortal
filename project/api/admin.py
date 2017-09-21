# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib.auth.models import User


# Register your models here.
admin.site.register(Session)
admin.site.register(School)
admin.site.register(Class)
admin.site.register(Subject)

admin.site.register(CustomUser)
admin.site.register(Principal)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Guardian)

