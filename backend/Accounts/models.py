from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField 

# this is needed because we extend AbstractBaseUser  
class CustomAccountManager(BaseUserManager):

    def create_superuser(self, username, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be superuser')

        return self.create_user(username, email, password, **other_fields)

    def create_user(self, username, email, password, **other_fields):
        # change email leter to lowercase
        email = self.normalize_email(email)
        
        user = self.model(username=username, email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=45, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    town = models.CharField(max_length=45, blank=True, null=True)
    telephone = PhoneNumberField(unique=True, blank=True, null=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    image = models.ImageField(blank=True, null=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomAccountManager()

    USERNAME_FIELD = 'username' 
    REQUIRED_FIELDS = ['email', 'country', 'town', 'telephone']

    def __str__(self):
        return self.username
