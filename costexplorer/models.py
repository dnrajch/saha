from django.db import models

# Create your models here.

class Customers(models.Model):
    customer_name = models.CharField(max_length=255)
    aws_user_id = models.CharField(max_length=25)
    aws_account = models.CharField(max_length=25)
    aws_user_arn = models.CharField(max_length=50)
    profile_pic = models.ImageField()

    
    