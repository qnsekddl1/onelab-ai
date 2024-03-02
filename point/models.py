from django.db import models

from member.models import Member
from oneLabProject.models import Period



class Point(Period):
    POINT_STATUS = [
        (1, '사용 중'),
        (2, '결제 완료'),
        (3, '결제 취소')
    ]

    point_status = models.SmallIntegerField(choices=POINT_STATUS)
    point = models.IntegerField(null=False, default=0)
    member = models.ForeignKey(Member, null=False, on_delete=models.PROTECT)
    class Meta:
        db_table = 'tbl_point'
        ordering = ['-id']