from django.db import models


# Create your models here.

class Projects(models.Model):
    project_name = models.CharField(max_length=100, blank=True)
    project_desc = models.CharField(max_length=300, blank=True)
    project_long_text = models.TextField(blank=True)
    project_features = models.JSONField(blank=True, default=list)
    project_link = models.URLField(blank=True)
    project_tech = models.CharField(max_length=200, blank=True)
    project_slug = models.SlugField(unique=True, blank=True)
    project_feature = models.BooleanField(default=False)
    project_thumbnail = models.ImageField(null=True, upload_to='portfolio/images/', blank=True)
    project_screenshot1 = models.ImageField(null=True, upload_to='portfolio/images/', blank=True)
    project_screenshot2 = models.ImageField(null=True, upload_to='portfolio/images/', blank=True)

