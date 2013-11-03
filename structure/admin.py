from django.contrib import admin
from structure.models import Organization, Member, Project, Role, Assignment, Contract

admin.site.register(Organization)
admin.site.register(Member)
admin.site.register(Project)
admin.site.register(Role)
admin.site.register(Assignment)
admin.site.register(Contract)
