from django.contrib import admin
from .models import Editor,Articles,tags

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Editor)
admin.site.register(Articles,ArticleAdmin)
admin.site.register(tags)