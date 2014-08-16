from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class Organization(models.Model):
    name = models.CharField(_('Name'), max_length=80)
    def __unicode__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(_('Name'), max_length=80)
    organization = models.ForeignKey('Organization')
    def __unicode__(self):
        return self.name

class User(AbstractUser):
    teams = models.ManyToManyField(Team, blank=True, related_name='users')
    def __unicode__(self):
        return self.username

class Contract(models.Model):
    name = models.CharField(_('Name'), max_length=150)
    organizations = models.ManyToManyField(Organization, through='ContractOrganization')
    def __unicode__(self):
        return self.name

class ContractOrganization(models.Model):
    contract = models.ForeignKey('Contract')
    organization = models.ForeignKey('Organization')
    default_team = models.ForeignKey('Team')
    def __unicode__(self):
        return self.contract.name + ' - ' + self.organization.name
    class Meta:
        verbose_name = _('Contracted organization')
        verbose_name_plural = _('Contracted organizations')

class ContractTeam(models.Model):
    contract = models.ForeignKey('Contract')
    team = models.ForeignKey('Team')
    def __unicode__(self):
        return self.contract.name + ' - ' + self.team.name
    class Meta:
        verbose_name = _('Contracted team')
        verbose_name_plural = _('Contracted teams')
