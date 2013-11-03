from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_tech = models.BooleanField(default=False)

class Organization(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Member(models.Model):
    user = models.ForeignKey('User')
    organization = models.ForeignKey('Organization')
    def __unicode__(self):
        return self.user.name + ' ' + self.organization.name

class Project(models.Model):
    organization = models.ForeignKey('Organization')
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Role(models.Model):
    organization = models.ForeignKey('Organization')
    is_tech = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Assignment(models.Model):
    user = models.ForeignKey('User')
    organization = models.ForeignKey('Organization')
    role =  models.ForeignKey('Role')
    def __unicode__(self):
        return self.user.name + ' ' + self.organization.name + ' ' . self.role.name

class Contract(models.Model):
    project = models.ForeignKey('Project')
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name
