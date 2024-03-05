from django.db import models

from file.models import File
from like.models import Like
from oneLabProject.models import Period
from point.models import Point
from review.models import Review
from university.models import University


class Share(Period):

    share_title = models.CharField(null=False, max_length=30)
    share_content = models.CharField(null=False, max_length=2000)
    share_points = models.BigIntegerField(null=True, default=1000)
    university = models.ForeignKey(University, on_delete=models.PROTECT, null=False)
    share_post_status = models.BooleanField(null=False, default=True)

    class Meta:
        db_table = 'tbl_share'
        ordering = ['id']


class ShareFile(Period):
    file = models.ForeignKey(File, primary_key=True,  on_delete=models.PROTECT, null=False)
    path = models.ImageField(null=False, blank=False, upload_to='share/%Y/%m/%d')
    share = models.ForeignKey(Share, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_share_file'


class ShareLike(Period):
    like = models.ForeignKey(Like, primary_key=True, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_share_like'

class SharePoints(Period):
    points = models.ForeignKey(Point, primary_key=True, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_share_points'

class ShareReview(Period):
    share = models.ForeignKey(Review, primary_key=True, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_share_review'