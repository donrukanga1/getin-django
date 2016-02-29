import datetime
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone
from model_utils.models import TimeStampedModel

class UserManager(BaseUserManager):
    def _create_user(self, username, phone_number, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
          raise ValueError('The given username must be set')
        user = self.model(username=username, phone_number=phone_number,
                 is_staff=is_staff, is_active=False,
                 is_superuser=is_superuser, last_login=now,
                 date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, phone_number=None, password=None, **extra_fields):
        return self._create_user(username, phone_number, password, False, False,**extra_fields)

    def create_superuser(self, username, phone_number, password, **extra_fields):
        user=self._create_user(username, phone_number, password, True, True, **extra_fields)
        user.is_active=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = (
        ('admin', 'admin'),
        ('vht', 'vht'),
        ('midwife', 'midwife'),
        ('dho', 'dho'),
    )
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=18)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    type = models.CharField(choices=USER_TYPES, max_length=120)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number',]

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name



class PregnantGirl(TimeStampedModel):
    MARITAL_STATUS_CHOICES = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced/Separated', 'Divorced/Separated'),
        ('Widowed', 'Widowed'),
    )
    EDUCATION_LEVEL_CHOICES = (
        ('None', 'None'),
        ('Primary', 'Primary'),
        ('Secondary', 'Secondary'),
        ('Tertiary', 'Tertiary'),
    )

    language_choices = (
        ('English', 'English'),
        ('Luganda', 'Luganda'),
    )

    contact_types = (
        ('Parent', 'Parent'),
        ('Guardian', 'Guardian'),
        ('Spouse', 'Spouse'),
        ('Sibling', 'Sibling'),
    )

    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    marital_status = models.CharField(max_length=255, choices=MARITAL_STATUS_CHOICES)
    education_level = models.CharField(max_length=255, choices=EDUCATION_LEVEL_CHOICES)
    emergency_contact = models.CharField(max_length=32, default="")
    contact_type = models.CharField(max_length=20, choices=contact_types, default="Parent")
    contact_number = models.CharField(max_length=13, default="")
    number_of_children = models.IntegerField(default=0)
    has_gone_for_anc = models.BooleanField(default=False)
    prefered_language = models.CharField(max_length=50, choices=language_choices, default='English')
    village = models.CharField(max_length=50, blank=True, null=True)
    parish = models.CharField(max_length=50, blank=True, null=True)
    subcounty = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.FloatField(default=-0.8195)
    longitude = models.FloatField(default=29.7426)
    mapped_by = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Pregnant Girls"


class AntenatalVist(TimeStampedModel):
    girl = models.ForeignKey(PregnantGirl)
    date = models.DateField()
    services = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.girl.name

class PresetMessage(models.Model):
    text = models.TextField(max_length=160)