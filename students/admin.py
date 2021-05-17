from import_export import resources
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Students


# Register your models here.

class StudentResource(resources.ModelResource):
    """used import_export admin for import and export in the admin panel"""
    class Meta:
        model = Students
        fields = ('registration_number', 'first_name', 'last_name', 'gender', 'date_of_admission', 'last_modified_date', 'id')


class StudentsAdmin(ImportExportModelAdmin):
    resource_class = StudentResource


admin.site.register(Students, StudentsAdmin)
