from django.db import models
from django.utils import timezone
from django.urls import reverse
import cloudinary.uploader
from cloudinary.models import CloudinaryField

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Use EmailField for validation

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the custom user model
    content = models.TextField()
    image = CloudinaryField("image", null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_posted']

    @classmethod
    def published(cls):
        return cls.objects.filter(is_published=True)

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, username, password=None, **extra_fields):
#         if not email:
#             raise ValueError("The email field must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email, username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, username, password, **extra_fields)

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=50, unique=True)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(default=timezone.now)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email

#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"

#     def get_short_name(self):
#         return self.first_name
    
    
# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     blogs = models.ManyToManyField(Blog)
    
#     @receiver(post_save, sender=True)
    
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)
            
#     @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    
#     def save_user_profile(sender, instance, **kwargs):
#         instance.profile.save()
