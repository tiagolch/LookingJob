from django.contrib import admin
from .models import AppliedCompanies, Documents, Interviews, Processes


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ['documents']


@admin.register(AppliedCompanies)
class AppliedCompaniesAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'position',
        'link',
        'active',
    ]
    list_filter = [
        'position',
        'active',
    ]


    admin.site.register(Interviews)
    admin.site.register(Processes)