
from django.contrib import admin
from django.urls import path, include
from core.views import (
    edit_subscription, 
    new_subscription, 
    list_subscriptions, 
    archive_or_active_subscription, 
    archived_subscriptions, 
    delete_subscription,
)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    # path('account/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('', new_subscription, name='new_subscription'),
    path('list_subscriptions/', list_subscriptions, name='list_subscriptions'),
    path('archived_subscriptions/', archived_subscriptions, name='archived_subscriptions'),
    path('edit_subscription/<int:pk>/', edit_subscription, name='edit_subscription'),
    path('archive_or_active_subscription/<int:pk>/', archive_or_active_subscription, name='archive_or_active_subscription'),
    path('delete_subscription/<int:pk>/', delete_subscription, name='delete_subscription'),
]
