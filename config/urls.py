from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path,include
from django.conf import settings  # setting.py ni import qildik
from django.conf.urls.static import static
schema_view = get_schema_view(
   openapi.Info(
      title="homework",
      default_version='v1',
      description="sayfullayev",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="1@gmail.com"),
      license=openapi.License(name="best"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/', include('apis.urls')),
    path('swagger.<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)