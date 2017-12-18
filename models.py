# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# default data model for monitapp..
class monit_data(models.Model):
    host = models.CharField(max_length=30)
    statusobject = models.CharField(max_length=30)
    querydate = models.DateField()
    querytime = models.TimeField()
    monitoringstatus = models.CharField(max_length=30)
    loadaverage = models.CharField(max_length=30)
    cpu = models.CharField(max_length=30)
    memoryusage = models.CharField(max_length=30)
    datacollected = models.CharField(max_length=30)

    def __unicode__(self):
	return self.name
