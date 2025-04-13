import debug_toolbar
from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("cinema.urls", namespace="cinema")),
    path("__debug__", include(debug_toolbar.urls)),
]
