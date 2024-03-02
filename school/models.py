from django.db import models
from member.models import Member
from oneLabProject.models import Period

class School(models.Model):
    member = models.ForeignKey(Member, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_school'
        ordering = ['-id']
