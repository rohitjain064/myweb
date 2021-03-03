from django.db import models
# from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.utils.timezone import now
# Create your models here.
class Type(models.Model):
    name=models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

class ExploreProject(models.Model):
    title = models.CharField(max_length=200)
    # subheadline=models.CharField(max_length=200,null=True,blank=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='explore_project_images', default='placeholder.png')
    body = RichTextUploadingField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    type = models.ManyToManyField(Type)
    # slug = models.SlugField(null=True, blank=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.title