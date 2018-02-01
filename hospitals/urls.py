from django.urls import include, path

from hospitals.views import HospitalListCreateView

app_name = 'hospitals'
urlpatterns = [
    path(r'', HospitalListCreateView.as_view(), name='list_create_hospitals')
]
