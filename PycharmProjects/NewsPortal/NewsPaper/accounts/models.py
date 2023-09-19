from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rating = models.IntegerField()

    def update_rating(self):
        articles_rate = Post.objects.filter(author_id=self.pk).aggregate(sum_articles=Sum('article_rating'))['sum_articles'] * 3
        comments_rate = Comment.objects.filter(user_id=self.users).aggregate(sum_comments=Sum('rating_comment'))['sum_comments'] or 0
        self.user_rating = articles_rate + comments_rate
        self.save()


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)

    politics = 'PL'
    sport = 'SP'
    general = 'GE'
    technologies = 'TC'
    fashion = 'FA'

    CAT = [
        (politics, 'Политика'),
        (sport, 'Спорт'),
        (general, 'Главная'),
        (technologies, 'Технологии'),
        (fashion, 'Мода')
    ]


class Post(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    time_news = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category', through='PostCategory')
    article = models.BooleanField(default=False)
    header = models.CharField(max_length=255)
    body = models.TextField()
    article_rating = models.IntegerField()

    def like(self):
        self.article_rating += 1
        self.save()

    def dislike(self):
        self.article_rating -= 1
        self.save()

    def preview(self):
        self.body = self.body[0:127] + '...'
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user_comment = models.CharField(max_length=255)
    time_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()


