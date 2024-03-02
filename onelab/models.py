from django.db import models

from file.models import File
from like.models import Like
from oneLabProject.models import Period
from university.models import University


class OneLab(Period):
    onelab_title = models.CharField(blank=False, null=False, max_length=50)
    onelab_content = models.CharField(blank=False, null=False, max_length=20)
    onelab_participate_url = models.CharField(blank=False, null=False, max_length=100)
    onelab_participate_group_id = models.IntegerField(null=False, blank=False)
    # 활동중: True, 탈퇴: False
    onelab_status = models.BooleanField(null=False, default=True)
    university = models.ForeignKey(University, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_onelab'
        ordering = ['-id']

class OneLabFile(Period):
    file = models.ForeignKey(File, primary_key=True, on_delete=models.PROTECT, null=False)
    path = models.ImageField(null=False, blank=False, upload_to='onelab/%Y/%m/%d')

    class Meta:
        db_table = 'tbl_onelab_file'

class OneLabBannerFile(Period):
    file = models.ForeignKey(File, primary_key=True, on_delete=models.PROTECT, null=False)
    path = models.ImageField(null=False, blank=False, upload_to='onelab_banner/%Y/%m/%d')

    class Meta:
        db_table = 'tbl_onelab_banner_file'

class OneLabLike(Period):
    like = models.ForeignKey(Like, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_onelab_like'