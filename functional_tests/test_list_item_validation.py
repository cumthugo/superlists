#from django.test import LiveServerTestCase
from unittest import skip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    #@skip
    def test_cannot_add_empty_list_items(self):
        self.fail('write me')
