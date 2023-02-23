from django.contrib import admin
from import_export.admin import *
from .models import *
 
# Register your models here.
class quizAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['question',  'op1','op2','op3','op4','op5']


admin.site.register(quiz, quizAdmin)

admin.site.register(dataset)
