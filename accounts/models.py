from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
# class MyUserManager(BaseUserManager):
#     def create_user(self, email, username, phone, password=None):
#         if not email:
#             raise ValueError('Email is Required')
#         if not username:
#             raise ValueError('Username is Required')
#         if not phone:
#             raise ValueError('Phone is Required')
#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#             phone=phone
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, username, phone, password=None):
#         user = self.create_user(
#             email=email,
#             username=username,
#             phone=phone,
#             password=password,
#         )
#         user.is_admin = True,
#         user.is_superuser = True,
#         user.save(using=self._db)
#         return user
#
#
# class MyUsers(AbstractBaseUser):
#     email = models.EmailField(verbose_name='email address', max_length=60, unique=True)
#     username = models.CharField(verbose_name='Username', max_length=60, unique=True)
#     phone = models.CharField(max_length=20, verbose_name='phone number')
#     date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
#     last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_transport = models.BooleanField(default=False)
#     is_driver = models.BooleanField(default=False)
#     is_staff_member = models.BooleanField(default=False)
#     is_hr = models.BooleanField(default=False)
#     is_workshop = models.BooleanField(default=False)
#     is_gpsa = models.BooleanField(default=False)
#
#
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email', 'phone']
#
#     objects = MyUserManager()
#
#     def __str__(self):
#         return self.username
#
#     def has_perm(self, perm, obj=None):
#         return True
#
#     def has_module_perms(self, app_label):
#         return True

# class Role(models.Model):
#     TRANSPORT = 1
#     DRIVER = 2
#     HR = 3
#     STAFF = 4
#     WORKSHOP = 5
#     GPSA = 6
#
#     id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)
#
#     def __str__(self):
#         return self.get_id_display()


class User(AbstractUser):
    USER_TYPE = (
        (1, 'Transport'),
        (2, 'Driver'),
        (3, 'hr'),
        (4, 'Staff'),
        (5, 'Workshop'),
        (6, 'Gpsa'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE, default=4)

    username = models.CharField(max_length=60, unique=True)






