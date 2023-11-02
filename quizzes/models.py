from django.db import models

# Create your models here.
class Calculator(models.Model):
    num1 = models.IntegerField
    op = models.TextField
    num2 = models.IntegerField
    output = models.IntegerField
    created_at = models.DateTimeField(auto_now_add=True)