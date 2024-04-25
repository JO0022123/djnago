from django.contrib import admin

# Register your models here.
from .models import *
class studentAdmin(admin.ModelAdmin):
    list_display=('name','email')
admin.site.register(student,studentAdmin)
admin.site.register(emp1)
admin.site.register(company)
admin.site.register(Product)