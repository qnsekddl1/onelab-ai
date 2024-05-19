from django.db import models
from oneLabProject.models import Period



class Tag(Period):
    TAG_STATUS = [
        (0, "공부"),
        (1, "친목"),
        (2, "수다"),
        (3, "공모전/대회")
    ]

    # TAG
    tag_name = models.SmallIntegerField(blank=False, null=False, max_length=50)

    class Meta:
        db_table = 'tbl_tag'
        ordering = ['created_date']

