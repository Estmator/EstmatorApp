from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.quote_view, name='api_quote'),
    ]
