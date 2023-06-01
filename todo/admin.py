from django.contrib import admin

from . models import ToDo, Tag


class ToDoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "created_at", "due_date", "status","tagged_with")
    list_display_links = ("id", "title")
    search_fields = ("title", "description", "status","tags__name")
    list_filter = ("status", "created_at", "due_date")
    list_per_page = 20

    fieldsets = (
        ("General", {
            "fields": ("title", "description", "status")
            }
        ),
        ("Date", {
            "fields": ("due_date",)
            }
        ),
        ("Tags", {
            "fields": ("tags",) 
            }
        )
    )

    def tagged_with(self, obj):
        return ", ".join([ tag.name for tag in obj.tags.all() ])


class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_per_page = 20
    list_filter = ("name",)

admin.site.register(ToDo, ToDoAdmin)
admin.site.register(Tag, TagAdmin)