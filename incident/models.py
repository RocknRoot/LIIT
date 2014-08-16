from django.db import models
from django.utils.translation import ugettext_lazy as _

class Issue(models.Model):
    title = models.CharField(_('Title'), max_length=150)
    description = models.TextField(_('Description'))
    contract = models.ForeignKey('structure.Contract')
    assigned_team = models.ForeignKey('structure.Team')
    assigned_user = models.ForeignKey('structure.User', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
