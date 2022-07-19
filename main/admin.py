from django.contrib import admin
from .models import Projects
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin



class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'

class CustomizedUserAdmin(UserAdmin):
    inlines = (AccountInline, )

# Register your models here.
admin.site.register(Projects)

admin.site.unregister(User)

admin.site.register(User, CustomizedUserAdmin)


# Register your models here.
