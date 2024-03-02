from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Category (models.Model):
    name = models.CharField(max_length=150)
    slug=models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)   #blank = False form içinde bos girilebilir
    
    def __str__(self):
        return self.name    
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)


class Blog(models.Model):

    title = models.CharField(max_length=200)
    image = models.CharField(max_length=50)
    description = RichTextField()
    full_description=RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug=models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)   #blank = False form içinde bos girilebilir
    category = models.ForeignKey(Category ,default=1, on_delete=models.CASCADE)    # on_delete=models.CASCADE -> category silindiginde ona ait bloglarda silinir
    # categories = models.ManyToManyField(Category)  many to many icin
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)



