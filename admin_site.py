import django.contrib.auth.admin
import django.contrib.flatpages.admin

# apps for admin
import profiles.admin
import records.admin
import snippets.admin
import django_basic_feedback.admin

# wysiwyg editor for flatpages
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from tinymce.widgets import TinyMCE

class TinyMCEFlatPageAdmin(FlatPageAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={
                    'theme':'advanced',
                    'theme_advanced_toolbar_location':'top',
                    'plugins':'fullscreen,style,table,spellchecker,paste,searchreplace',
                },
            ))
        return super(TinyMCEFlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, TinyMCEFlatPageAdmin)
