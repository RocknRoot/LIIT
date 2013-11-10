from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from structure.models import User, Organization, Member, Project, Role, Assignment, Contract
from incident.models import IssueStatus
from django.utils.translation import ugettext_lazy as _

class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Login'), {
            'fields': ['username', 'password', 'is_active', 'last_login']
        }),
        (_('Basic information'), {
            'fields': ['first_name', 'last_name', 'email', 'is_staff', 'is_superuser', 'date_joined']
        }),
        (_('Liit'), {
            'fields': ['is_tech']
        }),
    )

class RoleInline(admin.TabularInline):
    model = Role

class MemberInline(admin.TabularInline):
    model = Member
    
class OrganizationAdmin(admin.ModelAdmin):
    inlines = [MemberInline, RoleInline]

class AssignmentInline(admin.TabularInline):
    model = Assignment

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(AssignmentInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'user':
            if request._obj_ is not None:
                field.queryset = field.queryset.filter(member=request._obj_.organization)
        if db_field.name == 'role':
            if request._obj_ is not None:
                field.queryset = field.queryset.filter(organization=request._obj_.organization)
        return field

class IssueStatusInline(admin.TabularInline):
    model = IssueStatus

class ProjectAdmin(admin.ModelAdmin):
    inlines = [AssignmentInline, IssueStatusInline]

    def get_inline_instances(self, request, obj=None):
        if obj is None:
            return []
        return super(ProjectAdmin, self).get_inline_instances(request, obj)

    def get_form(self, request, obj=None, **kwargs):
        request._obj_ = obj
        return super(ProjectAdmin, self).get_form(request, obj, **kwargs)

admin.site.unregister(Site)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Contract)
