from django.contrib import admin
from blog.models import Post, Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = [
        'id',
        'title',
        'published_date',
        'is_published',
        'slug',
        'category'
    ]

    list_display_links = ['id', 'slug']
    list_filter = ['is_published', ]
    search_fields = ['title', 'content', 'slug']
    list_per_page = 25
    date_hierarchy = 'published_date'
