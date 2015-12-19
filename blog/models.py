from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256)
    teaser = models.CharField(max_length=256, blank=True, null=True)
    content = models.TextField()
    header = models.ImageField(blank=True, null=True)

    # Meta Info
    published_date = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, null=True)
    tags = TaggableManager()
    category = models.ForeignKey('Category', blank=True, null=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
