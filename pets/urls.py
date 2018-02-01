from django.urls import path

from pets.views import AnimalListCreateView

app_name = 'pets'
urlpatterns = [
    path(r'', AnimalListCreateView.as_view(), name='list_create_pets')
]
