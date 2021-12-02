from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path("i18n/", include("django.conf.urls.i18n")),
    path(settings.ADMIN_URL, admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # API base url
    path("api/v1/", include("config.api_v1")),
]

# if settings.DEBUG:
#     # This allows the error pages to be debugged during development, just visit
#     # these url in browser to see how these error pages look like.
#     urlpatterns += [
#         path(
#             "400/",
#             default_views.bad_request,
#             kwargs={"exception": Exception("Bad Request!")},
#         ),
#         path(
#             "403/",
#             default_views.permission_denied,
#             kwargs={"exception": Exception("Permission Denied")},
#         ),
#         path(
#             "404/",
#             default_views.page_not_found,
#             kwargs={"exception": Exception("Page not Found")},
#         ),
#         path("500/", default_views.server_error),
#     ]
#     if "debug_toolbar" in settings.INSTALLED_APPS:
#         import debug_toolbar

#         urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
