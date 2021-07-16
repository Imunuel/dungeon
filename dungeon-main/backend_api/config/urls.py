from django.conf import settings
from django.urls import path, include, re_path
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework.authtoken import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from graphene_django.views import GraphQLView


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


apipatterns = [
    path('paths/', include('paths.urls')),
    path('users/', include(('users.urls', 'users'))),
    path('dungeons/', include('dungeons.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(apipatterns)),
    path('auth/', views.obtain_auth_token),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('graphql', GraphQLView.as_view(graphiql=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
