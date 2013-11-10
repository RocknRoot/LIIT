from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):
    is_tech = models.BooleanField(_('Is resource ?'), default=False)
    def __unicode__(self):
        return self.username

class Organization(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = _('Organization')

class Member(models.Model):
    user = models.ForeignKey('User')
    organization = models.ForeignKey('Organization')
    def __unicode__(self):
        return self.user.username + ' - ' + self.organization.name
    class Meta:
        verbose_name = _('Member')

class Project(models.Model):
    organization = models.ForeignKey('Organization')
    name = models.CharField(_('Name'), max_length=100)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = _('Project')

class Role(models.Model):
    organization = models.ForeignKey('Organization')
    is_tech = models.BooleanField(_('Is resource-type role ?'), default=False)
    name = models.CharField(_('Name'), max_length=100)
    def __unicode__(self):
        return self.organization.name + ' - ' + self.name
    class Meta:
        verbose_name = _('Role')

class Assignment(models.Model):
    user = models.ForeignKey('User')
    project = models.ForeignKey('Project')
    role =  models.ForeignKey('Role')
    def __unicode__(self):
        return self.user.username + ' - ' + self.project.name + ' - ' . self.role.name
    class Meta:
        verbose_name = _('Assignment')

class Contract(models.Model):
    project = models.ForeignKey('Project')
    name = models.CharField(_('Name'), max_length=100)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = _('Contract')
