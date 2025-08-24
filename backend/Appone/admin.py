from django.contrib import admin
from .models import ExampleModel
## register

# Register your models here.
@admin.register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')