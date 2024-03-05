from django.db import models

from community.managers import CommunityManager
from file.models import File
from like.models import Like
from member.models import Member
from oneLabProject.models import Period


class Community(Period):
    COMMUNITY_STATUS = [
        (-1, '기타'),
        (0, '자료유형'),
        (1, '질문')
    ]

    community_title = models.CharField(null=False, max_length=30)
    community_content = models.CharField(null=False, max_length=2000)
    community_status = models.SmallIntegerField(choices=COMMUNITY_STATUS, default=0)
    member = models.ForeignKey(Member, on_delete=models.PROTECT, null=False)
    # True=게시 중, False=게시 종료
    community_post_status = models.BooleanField(null=False, default=True)

    objects = models.Manager()
    enabled_objects = CommunityManager()

    class Meta:
        db_table = 'tbl_community'
        ordering = ['-id']

class CommunityFile(Period):
    file = models.ForeignKey(File, primary_key=True, on_delete=models.PROTECT, null=False)
    path = models.ImageField(null=False, blank=False, upload_to='community/%Y/%m/%d')

    class Meta:
        db_table = 'tbl_community_file'

class CommunityLike(Period):
    like = models.ForeignKey(Like, primary_key=True, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_community_like'
