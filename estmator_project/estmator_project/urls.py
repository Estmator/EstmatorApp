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
    url(r'^api/v1/', include('est_api.urls')),
    url(r'^quote/$', views.QuoteView.as_view(), name='quote'),
    url(r'^quote/review$', views.review_quote_view, name='review'),
    url(r'^quote/form$', views.quote_form_view, name='quote_form'),
    url(r'^quote/send/(?P<pk>\d+)$', views.quote_email, name='send_quote'),
    url(
        r'^quote/(?P<token>[a-z0-9]{8}(-[a-z0-9]{4}){3}-[a-z0-9]{12})$',
        views.review_quote_view,
        name='quote_from_token'),
    url(
        r'^quote/form/edit$',
        views.quote_edit_form_view,
        name='quote_edit_form'),
    url(
        r'^client/form$',
        views.client_form_view,
        name='client_form'),
    url(
        r'^client/form/edit$',
        views.client_edit_form_view,
        name='client_edit_form'),
    url(
        r'^client/listform$',
        views.client_list_form_view,
        name='client_list_form'),
    url(r'^menu/$', views.menu_view, name='menu')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
