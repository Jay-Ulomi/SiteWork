from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    
    username = None
    ROLE_CHOICES = [
        ('admin','Admin'),
        ('staff','Staff'),
        ('worker','Worker'),
    ]
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='worker',
    )
    
    USERNAME_FIELD = 'email',
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    
