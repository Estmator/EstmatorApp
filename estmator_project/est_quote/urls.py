from django.conf.urls import url
import views

urlpatterns = [
    url(r'^calculate$', views.calc_view, name='api_calc'),
    ]
