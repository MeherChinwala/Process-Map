# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Bftbl(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version')
    proc = models.ManyToManyField('Proctbl', through='Bfproc', related_name='bus_func')


    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'bftbl'


class Domaintbl(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version')  # Field name made lowercase.
    bfs = models.ManyToManyField(Bftbl, through='Dombf', related_name='domain' )

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'domaintbl'


class Proctbl(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    Process = models.CharField(db_column='Process', max_length=100)  # Field name made lowercase.
    complexity = models.CharField(max_length=100, blank=True, null=True)
    criticality = models.CharField(max_length=100, blank=True, null=True)
    responsible_program = models.CharField(max_length=100, blank=True, null=True)
    version = models.IntegerField()
    sub_proc = models.ManyToManyField('Subproctbl', through='Procsubproc', related_name='proc')
    
    def __str__(self):
        return self.Process
        
    
    class Meta:
        managed = False
        db_table = 'proctbl'







class Subproctbl(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    subprocess = models.CharField(db_column='subProcess', max_length=100)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    resapplmodule = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=40, blank=True, null=True)


    def __str__(self):
        return self.subprocess
        
    class Meta:
        managed = False
        db_table = 'subproctbl'




class Dombf(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    domid = models.ForeignKey(Domaintbl, on_delete=models.CASCADE, db_column='Domid', max_length=100)
    bf = models.ForeignKey(Bftbl, on_delete=models.CASCADE, db_column='Bf', max_length=100)

    class Meta:
        managed = False
        db_table = 'dombf'

    def __str__(self):
        return self.id     



class Procsubproc(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    process = models.ForeignKey(Proctbl, related_name='map')  # Field name made lowercase.
    subprocess = models.ForeignKey(Subproctbl, related_name='map')  # Field name made lowercase.
    domain = models.ForeignKey(Domaintbl)

    class Meta:
        managed = False
        db_table = 'procsubproc'




class Bfproc(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    bf = models.ForeignKey(Bftbl, related_name='map0') # Field name made lowercase.
    process = models.ForeignKey(Proctbl, related_name='map0')  # Field name made lowercase.
    domain = models.ForeignKey(Domaintbl)

    class Meta:
        managed = False
        db_table = 'bfproc'
