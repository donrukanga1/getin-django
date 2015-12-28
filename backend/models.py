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
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    marital_status = models.CharField(max_length=255, choices=MARITAL_STATUS_CHOICES)
    education_level = models.CharField(max_length=255, choices=EDUCATION_LEVEL_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Pregnant Girls"