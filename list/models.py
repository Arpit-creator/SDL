from django.db import models
from accounts.models import User
import uuid

# Create your models here.
class todo_list(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
	heading = models.CharField(max_length=120, default='Plan for today')

	def __str__(self):
		return self.id

class list_item(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	item_of = models.ForeignKey(todo_list, on_delete=models.CASCADE, related_name='item_of')
	value = models.TextField(default='None')
	done = models.BooleanField(default=False)

	def __str__(self):
		return self.id
