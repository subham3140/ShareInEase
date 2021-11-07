from django.db import models
from .manager import NewBaseManager
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(verbose_name="email", unique=True, max_length=100)
    profile = models.ImageField(upload_to = "profile", verbose_name="profile pic")
    phone = models.CharField(max_length=14, verbose_name="phone number", null=True)
    specialist = models.CharField(max_length=500, blank=True, verbose_name="subject specialist")
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']    

    objects = NewBaseManager()

    def __str__(self):
        return self.username

    def has_module_perms(sel, app_lebel):
        return True
    
    def has_perm(self, perm, obj=None):
        return self.is_admin


class FileModel(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=100)
    file = models.FileField(upload_to="files", max_length=500)
    uploaded_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    about = models.TextField()

    def __str__(self) -> str:
        return f"{self.user.username}-{self.file_name}"