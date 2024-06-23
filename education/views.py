from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Category, SubCategory, Course, ContentType, CourseContent
from .serializers import CategorySerializer, SubCategorySerializer, CourseSerializer, ContentTypeSerializer, CourseContentSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ContentTypeViewSet(viewsets.ModelViewSet):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer


class CourseContentViewSet(viewsets.ModelViewSet):
    queryset = CourseContent.objects.all()
    serializer_class = CourseContentSerializer
