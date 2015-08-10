from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    # url(r'^api/v1/', include('est_api.urls')),
    # url(r'^client/', include('est_client.urls')),
    # url(r'^profile/', include('est_profile.urls')),
    # url(r'^quote/', include('est_quote.urls')),
    url(r'^quote/$', views.QuoteView.as_view(), name='quote'),
    url(r'^menu/$', views.MenuView.as_view(), name='menu')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
