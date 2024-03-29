from django.contrib import admin
from .models import Blog,Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","slug")
    list_editable = ("is_active" , "is_home",)
    search_fields=("title","description")
    readonly_fields=("slug",)
    list_filter=("category","slug")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug")
    search_fields=("name","slug")
    readonly_fields=("slug",)

admin.site.register(Blog , BlogAdmin)
admin.site.register(Category , CategoryAdmin)
