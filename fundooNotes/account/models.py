from django.db import models

# Create your models here.
class UserDetail(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    userName = models.CharField(max_length=40)
    email = models.EmailField(max_length = 25) 
    password = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
