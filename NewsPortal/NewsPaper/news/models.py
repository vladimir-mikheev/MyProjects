from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.urls import reverse


class News(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='news')
    author = models.ForeignKey(to='Author1', on_delete=models.CASCADE)
    pub_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])

    class Meta:
        ordering = ['-pub_date']  # новости выводятся в порядке от более свежей к самой старой



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()



class Author1(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name.title()