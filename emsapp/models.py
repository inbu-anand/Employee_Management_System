from django.db import models

# Create your models here.

class Employee(models.Model):
    empnumber = models.IntegerField()
    empname = models.CharField(max_length=50)
    empmail = models.EmailField(max_length=50)
    empcity = models.CharField(max_length=100)


    def __str__(self):
        return f"Employee:{self.empname}"