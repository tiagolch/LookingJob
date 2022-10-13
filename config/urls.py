
from django.contrib import admin
from django.urls import path, include
from core.views import edit_subscription, new_subscription, list_subscriptions, archive_subscription

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', new_subscription, name='new_subscription'),
    path('list_subscriptions/', list_subscriptions, name='list_subscriptions'),
    path('edit_subscription/<int:pk>/', edit_subscription, name='edit_subscription'),
    path('archive_subscription/<int:pk>/', archive_subscription, name='archive_subscription'),
]
