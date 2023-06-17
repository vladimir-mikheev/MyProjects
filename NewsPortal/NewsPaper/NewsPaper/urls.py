from django.contrib import admin
from django.urls import path, include
from accounts.views import login_view

urlpatterns = [
   path('admin/', admin.site.urls),
   path('login/', login_view, name='login'),
   path('pages/', include('django.contrib.flatpages.urls')),
   path('news/', include('news.urls')),
   path('articles/', include('news.urls'))
]
