from django.contrib import admin
from ad_snippets.models import Tag,Snippet

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    pass
