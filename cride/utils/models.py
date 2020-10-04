"""" Django models utilities"""

#django
from django.db import models

class CRideModel(models.Model):
    """share ride base model.

    CRideModel acts as an abstract basse class from wich every 
    other model in the project will inherit. This class provides 
    every table with the following attributes
        + creted(DateTime) : Store the datetime the object was created
        + modify(DateTime) : Store the datetime the object was modified
    """
    created = models.DateField(
        'created at', 
        auto_now_add=True
        help_text='Date time on wich the object was created.'
    )
    
    modified = models.DateField(
        'modified at', 
        auto_now=True
        help_text='Date time on wich the object was last modified.'
    )

    class Meta:
        """Meta option"""
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created','-modified']