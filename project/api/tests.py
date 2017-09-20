# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import *

# Create your tests here.
class UserTestCase(TestCase):

    def setUp(self):
        self.user_name = 'gf'
