from django.db import models
from .utils import convert_name_to_slug, random_color
from django_resized import ResizedImageField


class ColorField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        return super(ColorField, self).formfield(**kwargs)

class Book(models.Model):  
    title_pt = models.CharField(null=True,max_length=250)
    isbn = models.CharField(null=True, max_length=250)
    title_en = models.CharField(blank=True, null=True, max_length=250)
    author = models.CharField(null=True, max_length=250)

    img_url = models.CharField(blank=True,null=True, max_length=500)
    description = models.CharField(null=True, max_length=500)
    slug = models.CharField(null=True, max_length=250)
    aff_link = models.CharField(null=True, max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def recommended_count(self):
        return self.influencer_who_recommends.count()
    def __str__(self):
        if self.title_pt is not None:
            return self.title_pt
        else:
            return self.title_en


    def save(self, *args, **kwargs):
        if (self.img_url is None) and (self.isbn is not None):
            self.img_url = f'http://covers.openlibrary.org/b/isbn/{self.isbn}-M.jpg'
        super(Book,self).save(*args, **kwargs)


class Tag(models.Model):
    tagname = models.CharField(null=False, max_length=250)
    color = ColorField(default='#ffffff')

    def __str__(self):
        return self.tagname + self.color

    def save(self, *args, **kwargs):
        self.color = random_color()
        super(Tag,self).save(*args,**kwargs)

class Influencer(models.Model):
    image = ResizedImageField(size=[1800, 1800], crop=['middle', 'center'],null=True, default='media/faustao.jpg')
    name = models.CharField(null=False, max_length=250)
    recommended_books = models.ManyToManyField(Book,blank=True, related_name='influencer_who_recommends')
    written_books = models.ManyToManyField(Book,blank=True, related_name='influencer_who_wrote')
    description = models.CharField(null=True, max_length=500)
    slug = models.CharField(null=True, max_length=250)
    tags = models.ManyToManyField(Tag, blank=True, related_name='influencer_tags')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    @property
    def book_count(self):
        return self.recommended_books.count()
        
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = convert_name_to_slug(self.name)
        super(Influencer,self).save(*args, **kwargs)

# Create your models here.

