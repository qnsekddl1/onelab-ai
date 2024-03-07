from django.db import models

from file.models import File
from like.models import Like
from oneLabProject.models import Period
from school.models import School


class Exhibition(Period):
    exhibition_title = models.CharField(null=False, max_length=40)
    exhibition_content = models.CharField(null=False, max_length=2000)
    # False=관리자, True=school
    exhibition_status = models.BooleanField(null=False, blank=False, default=True)
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    # True=게시 중, False=게시 종료
    exhibition_post_status = models.BooleanField(null=False, default=True)

    class Meta:
        db_table = 'tbl_exhibition'
        ordering = ['-id']

class ExhibitionFile(Period):
    file = models.ForeignKey(File, primary_key=True, on_delete=models.PROTECT, null=False)
    path = models.ImageField(null=False, blank=False, upload_to='exhibition/%Y/%m/%d')
    exhibition = models.ForeignKey(Exhibition, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_exhibition_file'

class ExhibitionLike(Period):
    like = models.ForeignKey(Like, primary_key=True, on_delete=models.PROTECT, null=False)
    class Meta:
        db_table = 'tbl_exhibition_like'