
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from core.api.viewsets import AppliedCompanyViewset, DocumentViewset
from core.views import (archive_or_active_subscription, archived_subscriptions,
                        delete_subscription, edit_subscription,
                        list_subscriptions, new_subscription)



routers = routers.DefaultRouter()

routers.register(r'documents', DocumentViewset, basename='document')
routers.register(r'companies', AppliedCompanyViewset, basename='companies')
routers.register(r'interviews', AppliedCompanyViewset, basename='interviews')
routers.register(r'processes', AppliedCompanyViewset, basename='processes')


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('accounts/', include('allauth.urls')),
    path('', new_subscription, name='new_subscription'),
    path('list_subscriptions/', list_subscriptions, name='list_subscriptions'),
    path('archived_subscriptions/',
        archived_subscriptions,
        name='archived_subscriptions'
    ),
    path('edit_subscription/<int:pk>/',
         edit_subscription, 
         name='edit_subscription'
    ),
    path('archive_or_active_subscription/<int:pk>/',
        archive_or_active_subscription,
        name='archive_or_active_subscription'
    ),
    path('delete_subscription/<int:pk>/',
        delete_subscription,
        name='delete_subscription'
    ),
    path('api/', include(routers.urls)),
]
