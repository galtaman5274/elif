from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubCategoryViewSet, CourseViewSet, ContentTypeViewSet, CourseContentViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'content_types', ContentTypeViewSet)
router.register(r'course_contents', CourseContentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
