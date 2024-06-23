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


class Major(models.Model):
    subcategory = models.ForeignKey(SubCategory, related_name='majors', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    background_image = models.ImageField(upload_to='major_backgrounds/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContentType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class MajorContent(models.Model):
    major = models.ForeignKey(Major, related_name='contents', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, related_name='major_contents', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    task_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
