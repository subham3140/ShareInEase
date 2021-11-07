from django.contrib import admin
from .models import User, FileModel
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(FileModel)

class UserAdminCustom(UserAdmin):
    list_display = ('email', 'username', 'phone')
    search_fields = ('email', 'username', 'phone')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, UserAdminCustom)