from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubCategoryViewSet, MajorViewSet, ContentTypeViewSet, MajorContentViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)
router.register(r'majors', MajorViewSet)
router.register(r'content_types', ContentTypeViewSet)
router.register(r'major_contents', MajorContentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
