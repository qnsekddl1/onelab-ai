from django.db import models


# Point 사용 매니저
class UsePointManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(point_status=1)