from django.db import models
from oneLabProject.models import Period



class Tag(Period):
    # 일반 이메일
    tag_name = models.CharField(blank=False, null=False, max_length=50)

    class Meta:
        db_table = 'tbl_tag'
        ordering = ['created_date']

