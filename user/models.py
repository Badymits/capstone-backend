from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from game.models import Lobby

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        
        user = self.model(username=username.strip(), email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password=None, **extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        
        user.is_admin       = True
        user.is_staff       = True
        user.is_superuser   = True
        
        user.save(using=self.db)
        return user
    
class CustomUser(AbstractBaseUser):

    email                   = models.EmailField(max_length=255, unique=True)
    first_name              = models.CharField(max_length=255, blank=True, null=True)
    last_name               = models.CharField(max_length=255, blank=True, null=True)
    date_joined             = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    in_game                 = models.ForeignKey(Lobby, on_delete=models.CASCADE, null=True)
    username = models.CharField(
        max_length=150, 
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits, and spaces only.',
        validators=[],
        error_messages={
            'unique': "A user with that username already exists.",
        },
        blank=True,
        null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
    objects = CustomUserManager()
    
    
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)
    
    def __str__(self):
        
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

