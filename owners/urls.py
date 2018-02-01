from django.urls import path

from owners.views import OwnerListCreateView

app_name = 'owners'
urlpatterns = [
    path(r'', OwnerListCreateView.as_view(), name='list_create_owners')
]
