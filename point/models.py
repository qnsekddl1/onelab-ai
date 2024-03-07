from django.db import models

from member.models import Member
from oneLabProject.models import Period



class Point(Period):
    POINT_STATUS = [
        (1, '사용'),
        (2, '충전'),
        (3, '적립'),
    ]

    point_status = models.SmallIntegerField(choices=POINT_STATUS)
    point = models.IntegerField(null=False, default=5)
    member = models.ForeignKey(Member, null=False, on_delete=models.PROTECT)
    class Meta:
        db_table = 'tbl_point'
        ordering = ['-id']