from operator import mod
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.core.files.storage import FileSystemStorage
from django.urls import reverse



'''UPLOAD_ROOT="app_media"
upload_storage = FileSystemStorage(location=UPLOAD_ROOT, base_url='/uploads')'''


# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = ( ('draft', 'Draft'),('published', 'Published'),)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body = models.TextField()
    body2 = models.TextField()
    publish = models.DateTimeField(auto_now_add=True,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    document = models.ImageField(upload_to='images' ) #storage=upload_storage
    document2 = models.ImageField(upload_to='images')
    hit_count = models.IntegerField(default=0)
    feature_blog = models.BooleanField(default=False)
    tags = TaggableManager()

    '''def get_absolute_url(self):
        return reverse("index") #fawebsite:post_detail" , args=[self.slug]'''
    
    def get_absolute_url(self):
        #return reverse("post_detail" , kwargs={"slug":self.slug }) 
        return reverse("post_detail", args=[self.slug ]  )

    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=512)
    email = models.CharField(max_length=512)
    subject = models.CharField(max_length=512)
    message = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("save_contact") 

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='blog_posts_comment', null=True)
    name = models.CharField(max_length=512)
    email = models.CharField(max_length=512)
    website = models.CharField(max_length=512)
    message = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("index")     

