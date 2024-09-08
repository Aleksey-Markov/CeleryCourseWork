
from django.contrib import admin
from django.urls import path
from django.urls import include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://example.com/terms/",
        contact=openapi.Contact(name="API Support", email="support@example.com"),
        license=openapi.License(name="BSD License"),
        external_docs=openapi.ExternalDocumentation(
            url="https://swagger.io/docs/open-api/introduction/",
            description="Find more info here",
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    ))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users', include('users.urls', namespace='users')),
    path('habits/', include('habits.urls', namespace='habits')),
]
