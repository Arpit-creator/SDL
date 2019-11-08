from django.contrib import admin
from .models import todo_list, list_item

# Register your models here.
class ListAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')

class ItemAdmin(admin.ModelAdmin):
	list_display = ('id', 'item_of')

admin.site.register(todo_list, ListAdmin)

admin.site.register(list_item, ItemAdmin)