from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap

from mywebsite.sitemaps import StaticViewSitemap


sitemaps = {
    "static": StaticViewSitemap,
}


def robots_txt(request):
    content = """User-agent: *
Allow: /

Sitemap: https://hosseinkhosravian.ir/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("robots.txt", robots_txt),
    path("", include("mywebsite.urls")),
]

