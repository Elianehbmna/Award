# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Profile,Project

class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Eliane= Profile(first_name = 'Habimana', last_name ='Eliane',email ='elianehabimana3@gmail.com')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.Eliane,Profile))