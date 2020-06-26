from django.contrib import admin
from .models import Post, Comment, UserProfile,Category
# Register your models here.

admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Category)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("body", "post", "created_date", "active")
    list_filter = ("active", "created_date")
    search_fields = ("email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, queryset):
        queryset.update(active=True)

