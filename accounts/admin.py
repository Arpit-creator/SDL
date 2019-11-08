from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class AccountAdmin(UserAdmin):
	fieldsets = ("Authentication", {
            'classes': ('wide',),
            'fields': ('username', 'password'),
        }),
	list_filter = ('active', 'staff', 'admin')
	search_fields = ('username',)
	list_display = ('username', 'active', 'staff', 'admin', 'last_login')
	filter_horizontal = ()

admin.site.register(User, AccountAdmin)
