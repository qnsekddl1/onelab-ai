from django.db import models

from community.models import Community
from member.models import Member
from oneLabProject.models import Period
from reply.managers import ReplyManager


class Reply(Period):

    reply_content = models.CharField(null=False, blank=False, max_length=2000)
    reply_depth = models.BigIntegerField(default=1, null=False)
    reply_group_id = models.SmallIntegerField(null=False, blank=False)
    member = models.ForeignKey(Member, on_delete=models.PROTECT, null=False)
    community = models.ForeignKey(Community, on_delete=models.PROTECT, null=False)
    # True=게시 중, False=게시 종료
    reply_post_status = models.BooleanField(null=False, default=True)

    objects = models.Manager()
    enabled_objects = ReplyManager()

    class Meta:
        db_table = 'tbl_reply'
        ordering = ['-id']

    def __str__(self):
        return self.reply_content