from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from structure.models import Organization, Team, User, Contract, ContractOrganization, ContractTeam
from django.utils.translation import ugettext_lazy as _

class TeamAdmin(admin.ModelAdmin):
    list_display = ['organization', 'name']
    list_display_links = ['name']
    list_filter = ['organization']

class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Login'), {
            'fields': ['username', 'password', 'is_active', 'last_login']
        }),
        (_('Basic information'), {
            'fields': ['first_name', 'last_name', 'email', 'is_superuser', 'date_joined']
        }),
        (_('Teams'), {
            'fields': ['teams']
        }),
    )

class ContractOrganizationInline(admin.TabularInline):
    model = ContractOrganization

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(ContractOrganizationInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'default_team':
            if request._obj_ is not None:
                field.query_set = field.query_set.filter(organization=request._obj_.organization)
        return field

class ContractAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = [ContractOrganizationInline]

    def get_form(self, request, obj=None, **kwargs):
        request._obj_ = obj
        return super(ContractAdmin, self).get_form(request, obj, **kwargs)

admin.site.unregister(Site)
admin.site.unregister(Group)
admin.site.register(Organization)
admin.site.register(Team, TeamAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Contract, ContractAdmin)
