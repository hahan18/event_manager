from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken import views

from EventApp.views import EventAPIView

schema_view = get_schema_view(
    openapi.Info(
        title="Event Manager API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # -------------------API---------------------------

    re_path(r'^api/v1/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^api/v1/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^api/v1/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Djoser authentication roots
    path('api/v1/auth/', include('djoser.urls'), name='auth_djoser'),
    re_path(r'^auth/', include('djoser.urls.authtoken'), name='djoser_re'),

    # DRF default auth token
    path('api/v1/token/auth/', views.obtain_auth_token, name='auth_default'),

    # Make event
    path('api/v1/event/create/', EventAPIView.as_view(), name='create_event'),
]
