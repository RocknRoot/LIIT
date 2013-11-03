from django.db import models

class IssueStatus(models.Model):
    project = models.ForeignKey('structure.Project')
    name = models.CharField(max_length=100)
    is_basic = models.BooleanField(default=False)
    def __unicode__(self):
        return self.name

class Issue(models.Model):
    project = models.ForeignKey('structure.Project')
    status = models.ForeignKey('IssueStatus')
    user_reporter = models.ForeignKey('structure.User', related_name='reporter')
    user_assigned = models.ForeignKey('structure.User', related_name='assigned')
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)
    def __unicode__(self):
        return self.name
