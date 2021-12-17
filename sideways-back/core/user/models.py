from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager


class UserManager(BaseUserManager):

    def create_user(self, email, chairid, department, hospital, password=None, **kwargs):
        if chairid is None:
            raise TypeError('Users must have a chairid.')
        if email is None:
            raise TypeError('Users must have an email.')
        if department is None:
            raise TypeError('Users must have a department.')
        if hospital is None:
            raise TypeError('Users must have a hospital.')

        user = self.model(department=department, hospital=hospital,
                          chairid=chairid, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user


# list all the fields that must be included in user
class User(AbstractBaseUser, PermissionsMixin):
    department = models.CharField(null=True, max_length=225)
    hospital = models.CharField(null=True, max_length=225)
    email = models.EmailField(
        db_index=True, unique=True, null=True, blank=True)
    chairid = models.IntegerField(default=0, db_index=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['chairid']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
