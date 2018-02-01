from django.urls import include, path

from vets.views import VetListCreateView

app_name = 'vets'
urlpatterns = [
    path(r'', VetListCreateView.as_view(), name='list_create_vets')
]
