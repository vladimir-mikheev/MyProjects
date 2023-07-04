from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone
from datetime import timedelta
from .models import News, Category


@receiver(post_save, sender=News)
def send_weekly_article_list(sender, instance, created, **kwargs):
    if created:
        week_ago = timezone.now() - timedelta(weeks=1)
        new_articles = News.objects.filter(pub_date__gte=week_ago)

        for category in Category.objects.all():
            subscribers = category.subscribers.all()
            if subscribers.exists():
                subject = f'Новые статьи за неделю в категории "{category.name}"'
                template = 'email/weekly_articles.html'
                context = {'category': category, 'articles': new_articles}
                email_body = render_to_string(template, context)
                recipient_list = [subscriber.email for subscriber in subscribers]
                send_mail(subject, '', 'from@example.com', recipient_list, html_message=email_body)
