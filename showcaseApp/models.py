from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='category_thumbs/', blank=True, null=True)


    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


MEDIA_CHOICES = (
    ('image', 'Image'),
    ('video', 'Video'),
)


class Project(models.Model):
    category = models.ForeignKey(Category, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=10, choices=MEDIA_CHOICES)
    media_file = models.FileField(upload_to='projects/')
    tagline = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.media_type})"