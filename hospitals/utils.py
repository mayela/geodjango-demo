from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D

from hospitals.models import Hospital

def closest_hospitals_by_location(latitude, longitude, distance=5):
    point_wkt = 'POINT({} {})'.format(longitude, latitude)
    point = GEOSGeometry(point_wkt, srid=4326)
    hospitals = Hospital.objects.filter(
        location__distance_lte=(
            point,
            D(km=distance)
            )
        )
    return hospitals
