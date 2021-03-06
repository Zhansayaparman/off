from django.contrib import admin

# Register your models here.

from .models import Admin, Office, Workers


# admin.site.register(Workers)
# admin.site.register(Admin)
# Define the admin class
#model
class AdminInstanceInline(admin.TabularInline):
    model = Workers


class workAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')
    inlines = [AdminInstanceInline]
    fields = ['first_name', 'last_name', ('date_of_birt')]


# админ классына регистрация жасаймыз
admin.site.register(Admin, workAdmin)

admin.site.register(Office)

@admin.register(Workers)
class WorkersAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'admin')

