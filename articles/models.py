from django.db import models
from django.utils.text import slugify


# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=40, default='defaulttag')

    def __str__(self):
        return self.tag


class Article(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, allow_unicode=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    text = models.TextField(default='')
    image = models.ImageField(upload_to='articles/', default='articles/none.png')

    class Meta:
        ordering = ['-date']

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return self.title
