from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.utils.timezone import now


# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=200)
    percent=models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=200)
    # subheadline=models.CharField(max_length=200,null=True,blank=True)
    thumbnail=models.ImageField(null=True,blank=True,upload_to='post_images',default='placeholder.png')
    body=RichTextUploadingField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=False)
    featured=models.BooleanField(default=False)
    tags=models.ManyToManyField(Tag)
    # slug=models.SlugField(null=True,blank=True)
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.title


    # def save(self,*args,**kwargs):
    #     if self.slug == None:
    #         slug=slugify(self.title)
    #         has_slug=Post.objects.filter(slug=slug).exists()
    #         count=1
    #         while has_slug:
    #             count+=1
    #             slug=slugify(self.title) + '-' +str(count)
    #             has_slug=Post.objects.filter(slug=slug).exists()
    #
    #         self.slug=slug
    #         super().save(*args, **kwargs)

class Contact(models.Model):
    name=models.CharField(max_length=150)
    subject=models.CharField(max_length=800)
    phone_no=models.PositiveIntegerField()
    email=models.EmailField()
    message=models.TextField()
    ip_address=models.GenericIPAddressField()
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return str(f"{self.name}-{self.email}")
