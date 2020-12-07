from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, userName,first_name, last_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not userName:
            raise ValueError('Users must have a userName')
        if not first_name:
            raise ValueError('Users must specify a first name')  
        if not last_name:
            raise ValueError('Users must specify a last name') 

        user = self.model(
            email=self.normalize_email(email),
            userName=userName,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, userName, first_name,last_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            userName=userName,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
 

class Account(AbstractBaseUser):
	email = models.EmailField(verbose_name="email", max_length=40, unique=True)
	userName = models.CharField(max_length=40, unique=True)
	date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['userName' , 'first_name' ,'last_name']

	objects = MyAccountManager()

	def __str__(self):
		return self.email

	# For checking permissions. 
	def has_perm(self, perm, obj=None):
		return self.is_admin

	
	def has_module_perms(self, app_label):
		return True


# Create your models here.
# class UserDetail(models.Model):
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     userName = models.CharField(max_length=40)
#     email = models.EmailField(max_length = 25) 
#     password = models.CharField(max_length=30)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.first_name
