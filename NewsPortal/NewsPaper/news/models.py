from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone


class News(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='news')
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    class Meta:
        ordering = ['-pub_date']  # новости выводятся в порядке от более свежей к самой старой


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()