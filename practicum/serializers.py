from rest_framework import serializers
from .models import Category, SubCategory, Major, ContentType, MajorContent

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'background_image']


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'category', 'name', 'description', 'background_image']


class MajorSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(read_only=True)

    class Meta:
        model = Major
        fields = ['id', 'subcategory', 'title', 'description', 'background_image', 'created_at', 'updated_at']


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = ['id', 'name', 'description']


class MajorContentSerializer(serializers.ModelSerializer):
    major = MajorSerializer(read_only=True)
    content_type = ContentTypeSerializer(read_only=True)

    class Meta:
        model = MajorContent
        fields = ['id', 'major', 'content_type', 'title', 'content', 'task_url', 'created_at', 'updated_at']
