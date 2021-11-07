from django.contrib.auth.models import BaseUserManager



class NewBaseManager(BaseUserManager):

    def create_user(self, email, username, password=None, **others):

        if not email:
            raise ValueError("Please Provide Email")

        if not username:
            raise ValueError("Please Provide Username")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            **others
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **others):

        others.setdefault('is_staff', True)
        others.setdefault('is_active', True)
        others.setdefault('is_superuser', True)
        others.setdefault('is_admin', True)

       
        return self.create_user(email, username, password, **others)
