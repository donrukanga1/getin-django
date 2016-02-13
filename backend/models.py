from django.db import models
from model_utils.models import TimeStampedModel

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