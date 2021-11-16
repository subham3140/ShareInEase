from django.db import models
from .manager import NewBaseManager
from django.contrib.auth.models import AbstractBaseUser
from django.utils.timezone import now
# Create your models here.

FILE_TYPE = (
    ("assignment", "ASSIGNMENT"),
    ("syllabus", "SYLLABUS"),
    ("report", "REPORT"),
    ("notice", "NOTICE"),
    ("result", "RESULT"),
    ("other", "OTHER")
)

class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(verbose_name="email", unique=True, max_length=100)
    profile = models.ImageField(upload_to = "profile", verbose_name="profile pic")
    phone = models.CharField(max_length=14, verbose_name="phone number", null=True)
    specialist = models.CharField(max_length=500, blank=True, verbose_name="subject specialist")
    address = models.CharField(max_length=1000, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    facebook_link = models.CharField(max_length=1000, blank=True, null=True)
    github_link = models.CharField(max_length=1000, blank=True, null=True)
    twitter_link = models.CharField(max_length=1000, blank=True, null=True)
    instagram_link = models.CharField(max_length=1000, blank=True, null=True)
    linkedin_link = models.CharField(max_length=1000, blank=True, null=True)

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
    file_type = models.CharField(max_length=50, blank=False, choices=FILE_TYPE, default=FILE_TYPE[3][0])
    uploaded_at = models.DateField(default=now)
    title = models.CharField(max_length=100)
    about = models.TextField(null=True, blank=True)
    qrcode = models.FileField(upload_to="media", null=True, blank=True)
    downloadurl = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user.username}-{self.file_name}"

    def filename(self) -> str:
        return (self.file.path).split("\r")[0].split("\\")[-1]
