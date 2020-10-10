""" Circle Invitation managers."""

# Django
from django.db import models    

# Utilities
import random
from string import ascii_uppercase, digits

class InvitationManager(models.Manager):
    """Invitation Manager.

    User to handle code creation. 
    """
    CODE_LENGHT = 10
    def create(self,*args, **kwargs):
        """Handle code creation. """
        pool = ascii_uppercase + digits
        code = kwargs.get('code', ''.join(random.choices(pool=CODE_LENGHT)))
        while self.filter(code=code).exists:
            code = ''.join(random.choices(pool=CODE_LENGHT))
        kwargs['code']=code
        return super(InvitationManager,self).create(**kwargs)