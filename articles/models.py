from django.db import models
from django.conf import settings
from django.utils.text import slugify


# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.tag


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=''
    )
    slug = models.SlugField(unique=True, allow_unicode=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    text = models.TextField(default='')
    image = models.ImageField(upload_to='articles/', default='NULL', null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return self.title
