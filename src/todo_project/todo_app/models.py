from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
        """Helps Django Works with our custom user models"""

        def create_user(self, email, name, password=None):
            """Create a new user profile object."""
            if not email:
                raise ValueError("Users must have an email Address")

            email = self.normalize_email(email)
            user  = self.model(email=email, name=name)

            user.set_password(password)
            user.save(using=self._db)

            return user
        def create_superuser(self, email, name, password):
            """Creates and saves a new super user with a given detaisl """

            user = self.create_user(email, name, password)

            user.is_superuser = True
            user.is_staff     = True
            user.save(using=self._db)
            return user


class UserProfile(AbstractBaseUser, PermissionsMixin):

        """Represent a "user profile" in our system."""
        email = models.EmailField(max_length=255, unique=True)
        name  = models.CharField(max_length=255)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)


        objects = UserProfileManager()

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['name']

        def get_full_name(self):
            """Used to get a users fullname"""


            return self.name

        def get_short_name(self):
           """used to get a users short name"""

           return self.name
        def __str__(self):
           """Django uses it when needs to convert object into string"""

           return self.email

class ProfileFeedItem(models.Model):

       """Profile status Update"""
       user_profile = models.ForeignKey('UserProfile', on_delete= models.CASCADE)
       status_text = models.CharField(max_length=255)
       created_on = models.DateTimeField(auto_now_add=True)

       def __str__(self):

           """Return model as string"""
           return self.status_text
