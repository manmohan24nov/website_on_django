from django.contrib import admin
from .models import tutorial
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

class TutorialAdmin(admin.ModelAdmin):

    fieldsets = [('Title/Contents', {'fields':['tutorial_title','tutorial_content']}),
                 ('Date',{'fields':['tutorial_published']})]

    formfield_overrides = {
        models.TextField : {
            'widget': TinyMCE()
        }
    }



admin.site.register(tutorial, TutorialAdmin)