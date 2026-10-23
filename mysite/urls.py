from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def robots_txt(request):
    content = """User-agent: *
Allow: /

Sitemap: https://hosseinkhosravian.ir/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("mywebsite.urls")),
    path("robots.txt", robots_txt),
]
