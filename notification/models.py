from django.db import models

from file.models import File
from oneLabProject.models import Period


class Notification(Period):
    NOTIFICATION_STATUS = [
        (0, '커뮤니티'),
        (1, '원랩'),
        (2, '장소공유'),
        (3, '대회공모전')
    ]
    notification_title = models.CharField(null=False, blank=False, max_length=30)
    notification_content = models.CharField(null=False, blank=False, max_length=2000)
    notification_view_count = models.IntegerField(null=False, blank=False, default=0)
    notification_status = models.SmallIntegerField(choices=NOTIFICATION_STATUS, default=0)
    # True=게시 중, False=게시 종료
    notification_post_status = models.BooleanField(null=False, default=True)


    class Meta:
        db_table = 'tbl_notification'
        ordering = ['-id']

class NotificationFile(Period):
    file = models.ForeignKey(File, primary_key=True, on_delete=models.PROTECT, null=False)
    path = models.ImageField(null=False, blank=False, upload_to='notification/%Y/%m/%d')

    class Meta:
        db_table = 'tbl_notification_file'