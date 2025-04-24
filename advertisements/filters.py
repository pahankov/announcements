import django_filters
from django_filters import DateFromToRangeFilter
from .models import Advertisement

class AdvertisementFilter(django_filters.FilterSet):
    created_at = DateFromToRangeFilter()
    status = django_filters.CharFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']
