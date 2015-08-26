from django.conf.urls import include, url

urlpatterns = [

    url(r'^client/', include('est_client.urls')),
    url(r'^profile/', include('est_profile.urls')),
    url(r'^quote/', include('est_quote.urls'))

]
