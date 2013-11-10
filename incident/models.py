from django.db import models
from django.utils.translation import ugettext_lazy as _

class IssueStatus(models.Model):
    project = models.ForeignKey('structure.Project')
    name = models.CharField(_('Name'), max_length=100)
    is_basic = models.BooleanField(_('Can clients use it ?'), default=False)
    def __unicode__(self):
        return self.project.name + ' - ' + self.name
    class Meta:
        verbose_name = _('Issue status')
        verbose_name_plural = _('Issue statuses')

class Issue(models.Model):
    project = models.ForeignKey('structure.Project')
    status = models.ForeignKey(_('Issue\'s status'), 'IssueStatus')
    user_reporter = models.ForeignKey('structure.User', related_name='reporter')
    user_assigned = models.ForeignKey('structure.User', related_name='assigned')
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'))
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)
    def __unicode__(self):
        return self.name
