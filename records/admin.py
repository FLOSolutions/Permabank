from django.contrib import admin
from records.models import Category, Record, Request, Wish


class CategoryAdmin(admin.ModelAdmin):
    """ Admin for records.Category """
    # auto-generate category slug from title:
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

for model in (Record, Request, Wish):
    admin.site.register(model)
