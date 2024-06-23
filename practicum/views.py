from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Category, SubCategory, Major, ContentType, MajorContent
from .serializers import CategorySerializer, SubCategorySerializer, MajorSerializer, ContentTypeSerializer, MajorContentSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class MajorViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer


class ContentTypeViewSet(viewsets.ModelViewSet):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer


class MajorContentViewSet(viewsets.ModelViewSet):
    queryset = MajorContent.objects.all()
    serializer_class = MajorContentSerializer
