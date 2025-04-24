from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


class Advertisement(models.Model):
    STATUS_OPEN = "OPEN"
    STATUS_CLOSED = "CLOSED"
    STATUS_CHOICES = [
        (STATUS_OPEN, "Открыто"),
        (STATUS_CLOSED, "Закрыто"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=6, choices=STATUS_CHOICES, default=STATUS_OPEN)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def clean(self):
        if self.status == self.STATUS_OPEN:
            open_ads_count = Advertisement.objects.filter(
                creator=self.creator,
                status=self.STATUS_OPEN
            ).exclude(id=self.id).count()

            if open_ads_count >= 10:
                raise ValidationError("У пользователя не может быть более 10 открытых объявлений.")
