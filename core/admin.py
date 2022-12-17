from django.contrib import admin
from .models import Companies, Documents


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ['documents']


@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'position',
        'interview_date',
        'aplication_status',
        'link',
        'active',
    ]
    list_filter = [
        'position',
        'interview_date',
        'aplication_status',
        'active',
    ]
