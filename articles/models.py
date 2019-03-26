from django.db import models


# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=40, default='defaulttag')

    def __str__(self):
        return self.tag


class Article(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateField(auto_now=True, auto_now_add=False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    text = models.TextField(default='')
    image = models.ImageField(upload_to='articles/', default='media/articles/none.png')

    def __str__(self):
        return self.title
