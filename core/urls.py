from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

from notification.api.views import NotificationView

router = routers.DefaultRouter()
#router.register(r'notifications', NotificationView)


schema_view = get_schema_view(
    openapi.Info(
        title="SereXon",
        default_version="v1",
        description="SereXon-endpoint (API) Project",
        contact=openapi.Contact(email="mwombekilubere@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("", include("custom.api.urls")),
    path("admin/", admin.site.urls),
    path("api/staff/", include("staff.api.urls")),
    path("api/student/", include("student.api.urls")),
    path("api/innovation/", include("innovation.api.urls")),
    path("api/research/", include("research.api.urls")),
    path("api/publication/", include("publication.api.urls")),
    path('api/custom/', include('rest_framework.urls')),
    path("api/", include("notification.api.urls")),
    path(
        "drf-api/docs",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
