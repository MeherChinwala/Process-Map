# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

admin.site.register(models.Bftbl)
admin.site.register(models.Proctbl)
admin.site.register(models.Subproctbl)
admin.site.register(models.Dombf)
admin.site.register(models.Domaintbl)
admin.site.register(models.Procsubproc)
admin.site.register(models.Bfproc)

# Register your models here.
