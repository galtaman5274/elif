from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    background_image = models.ImageField(upload_to='category_backgrounds/', blank=True, null=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    background_image = models.ImageField(upload_to='subcategory_backgrounds/', blank=True, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    subcategory = models.ForeignKey(SubCategory, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    background_image = models.ImageField(upload_to='course_backgrounds/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContentType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class CourseContent(models.Model):
    course = models.ForeignKey(Course, related_name='contents', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, related_name='course_contents', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    exercises = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
