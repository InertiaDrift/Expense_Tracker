from django.contrib import admin
from .models import Expense, Categories, Tags

# Register your models here.

admin.site.register(Expense)
admin.site.register(Categories)
admin.site.register(Tags)
