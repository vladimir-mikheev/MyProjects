from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User


def send_article_email(article):
    users = User.objects.filter(subscribed_categories=article.category)

    for user in users:
        subject = article.name
        message = f"Здравствуй, {user.username}. Новая статья в твоём любимом разделе!"
        link = 'http://127.0.0.1:8000/articles/{}'.format(article.id)
        html_message = render_to_string('article_notification.html', {'article': article, 'user': user})
        send_mail(subject, message, None, [user.email], html_message=html_message)
