
from django.contrib import admin
from django.urls import path
from core.views import new_subscription

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', new_subscription, name='new_subscription'),
]
