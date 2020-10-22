from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Squirrel(models.Model):
    X=models.FloatField(
            help_text=_('Longtitude'),
            )
    Y=models.FloatField(
            help_text=_('Latitude'),
            )
    unique_id=models.CharField(
            max_length=200,
            help_text=_('Squirrel ID'),
            primary_key=True,)

    AM='AM'
    PM='PM'
    SHIFT_CHOICES=[
            (AM,_('AM')),
            (PM,_('PM')),
            ]
    shift=models.CharField(
            max_length=100,
            help_text=_('Shift'),
            choices=SHIFT_CHOICES,
            null=True
            )


    date=models.DateField(
            help_text=('Date'),
            )

    J='Juvenile'
    A='Adult'
    AGE_CHOICES=[
            (J,_('Juvenile')),
            (A,_('Adult')),
            ]
    age=models.CharField(
            max_length=100,
            help_text=_('Age'),
            choices=AGE_CHOICES,
            null=True
            )

    def __str__(self):
        return self.unique_id








