from django.contrib import admin
from .models import Category, SubCategory, Course, ContentType, CourseContent

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'background_image')
    search_fields = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'background_image')
    search_fields = ('name', 'category__name')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subcategory', 'description', 'background_image', 'created_at', 'updated_at')
    search_fields = ('title', 'subcategory__name')
    list_filter = ('subcategory', 'created_at')


@admin.register(ContentType)
class ContentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


@admin.register(CourseContent)
class CourseContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course', 'content_type', 'created_at', 'updated_at')
    search_fields = ('title', 'course__title')
    list_filter = ('course', 'content_type', 'created_at')
