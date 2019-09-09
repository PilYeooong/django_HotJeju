from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'address', 'created', 'updated']
    prepopulated_fields = {'slug':('name',)}
    list_filter = ['created', 'updated', 'category']
admin.site.register(Place, PlaceAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','author', 'places' , 'text']
admin.site.register(Comment, CommentAdmin)

admin.site.register(Notice)