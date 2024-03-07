from django.db import models
from member.models import Member
from oneLabProject.models import Period

class School(models.Model):
    member = models.ForeignKey(Member, on_delete=models.PROTECT, null=False)
    school_member_address = models.CharField(max_length=500, null=False, blank=False, default='서울시 강남구')
    school_name = models.CharField(null=False, blank=False, max_length=100)

    class Meta:
        db_table = 'tbl_school'
        ordering = ['-id']