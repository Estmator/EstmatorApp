from django.conf.urls import url
import views

urlpatterns = [
    # urls begin with /client/

    url(r'^$', views.client_view, name='api_client'), # not sure what the api urls are doing currently

    url(
        r'^form$',
        views.client_form_view,
        name='client_form'
    ),
    url(
        r'^form/edit$',
        views.client_edit_form_view,
        name='client_edit_form'
    ),
    url(
        r'^listform$',
        views.client_list_form_view,
        name='client_list_form'
    )

]
