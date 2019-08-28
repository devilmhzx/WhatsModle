import random

from django.test import TestCase

# Create your tests here.

randomfont = random.sample('abcdefghijklmnopqrstuvwxyz', 5)

print(randomfont)