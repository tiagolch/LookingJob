
from django.contrib import admin
from django.urls import path, include
from core.views import new_subscription

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', new_subscription, name='new_subscription'),
    path('accounts/', include('django.contrib.auth.urls')),
]
