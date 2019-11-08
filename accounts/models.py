from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, password=None, is_Staff=False, is_Admin=False, is_Active=True):
        if not(password):
            raise ValueError('Users must have a password')
        if not(username):
            raise ValueError('Users must have a username')
        user_obj = self.model(
            username = username,
        )
        user_obj.set_password(password)
        user_obj.staff = is_Staff
        user_obj.admin = is_Admin
        user_obj.active = is_Active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, username, password=None):
        user_obj = self.create_user(
            username=username,
            password=password,
            is_Staff=True,
        )
        return user_obj

    def create_superuser(self, username, password=None):
        user_obj = self.create_user(
            username=username,
            password=password,
            is_Admin=True,
            is_Staff=True,
        )
        return user_obj

class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=120, default=None, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def follower_group_user(self):
        return self.username