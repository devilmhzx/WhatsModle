from django.db import models

# Create your models here.

class UserRegister(models.Model):
    uname = models.CharField(max_length=20,unique=True,null=False)
    upwd = models.CharField(max_length=20, null=False)




