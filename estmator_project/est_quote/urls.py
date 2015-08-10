from django.conf.urls import url
import views

urlpatterns = [
    url(r'^add/$', views.QuoteCreateView.as_view(), name='add_quote'),
    # url(r'^edit/$', views.QuoteEditView.as_view(), name='edit_quote'),
]
