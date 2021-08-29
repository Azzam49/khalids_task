from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from task.app.models import User


class CustomUserAdmin(admin.ModelAdmin):

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.register(User, CustomUserAdmin)
