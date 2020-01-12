# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Poll(models.Model):

    name = models.CharField(max_length=30)
    about = models.CharField(default='-',max_length=30)

    fb = models.CharField(default='-',max_length=30)
    tv = models.CharField(default='-',max_length=30)
    ln = models.CharField(default='-',max_length=30)
    

    set_name = models.CharField(default='-',max_length=30)
    
    def __str__(self):
        return self.set_name + " | " + str(self.pk)

