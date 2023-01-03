import uuid
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


SHIFT_CHOICES = (
    ('00:00:00-08:00:00', '00:00:00-08:00:00'),
    ('08:00:00-16:00:00', '08:00:00-16:00:00'),
    ('16:00:00-00:00:00', '16:00:00-00:00:00'),
)


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name="name", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    department = models.CharField(max_length=70)
    position = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin


class UserShift(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES)
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        unique_together = ('user', 'date')
    
    def __str__(self):
        return f'{self.user.username} {self.date} {self.shift}'