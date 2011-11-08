from django.contrib import admin
from records.models import Category, Record, Gift, Wish


class CategoryAdmin(admin.ModelAdmin):
    """ Admin for records.Category """
    # auto-generate category slug from title:
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

for model in (Record, Gift, Wish):
    admin.site.register(model)
