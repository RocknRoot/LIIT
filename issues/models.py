from django.db import models

class Status(models.Model):
    title = models.CharField(max_length=200)
    priority = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)

class Type(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)

class Issue(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    type = models.ForeignKey(Type)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)

class FollowUp(models.Model):
    comment = models.TextField()
    parent_issue = models.ForeignKey(Issue)
    public = models.BooleanField(default=True)
    status_from = models.ForeignKey(Status, null=True, on_delete=models.PROTECT, related_name='+')
    status_to = models.ForeignKey(Status, null=True, on_delete=models.PROTECT, related_name='+')
    type_from = models.ForeignKey(Type, null=True, related_name='+')
    type_to = models.ForeignKey(Type, null=True, related_name='+')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)

class Workflow(models.Model):
    status_from = models.ForeignKey(Status, related_name='+')
    status_to = models.ForeignKey(Status, related_name='+')
    type = models.ForeignKey(Type)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)
