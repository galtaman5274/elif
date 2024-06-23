from rest_framework import serializers
from .models import Category, SubCategory, Course, ContentType, CourseContent

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'background_image']


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'category', 'name', 'description', 'background_image']


class CourseSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'subcategory', 'title', 'description', 'background_image', 'created_at', 'updated_at']


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = ['id', 'name', 'description']


class CourseContentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    content_type = ContentTypeSerializer(read_only=True)

    class Meta:
        model = CourseContent
        fields = ['id', 'course', 'content_type', 'title', 'content', 'video', 'exercises', 'created_at', 'updated_at']
        extra_kwargs = {
            'video': {'required': False, 'allow_null': True},
        }
