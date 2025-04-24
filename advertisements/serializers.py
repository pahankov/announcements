from rest_framework import serializers
from .models import Advertisement

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'description', 'creator', 'status', 'created_at']
        read_only_fields = ['creator', 'created_at']

    def validate(self, data):
        if self.instance is None and data.get('status') == 'OPEN':
            user = self.context['request'].user
            if Advertisement.objects.filter(creator=user, status='OPEN').count() >= 10:
                raise serializers.ValidationError("Нельзя иметь больше 10 открытых объявлений.")
        return data
