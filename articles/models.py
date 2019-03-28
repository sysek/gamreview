from django.db import models


# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=40, default='defaulttag')

    def __str__(self):
        return self.tag


class Article(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    text = models.TextField(default='')
    image = models.ImageField(upload_to='articles/', default='articles/none.png')

    class Meta:
        ordering = ['-date',]

    def __str__(self):
        return self.title
