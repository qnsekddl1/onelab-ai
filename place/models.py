from django.db import models

from file.models import File
from like.models import Like
from oneLabProject.models import Period
from point.models import Point
from review.models import Review
from school.models import School


class Place(Period):

    place_title = models.CharField(null=False, max_length=30)
    place_content = models.CharField(null=False, max_length=300)
    place_points = models.BigIntegerField(null=True, default=1000)
    # False=결제 전, True=결제완료
    place_order_status = models.BooleanField(null=False, default=False)
    place_review_rating = models.FloatField(null=False, default=0.0)
    place_image_file = models.ImageField(null=False, blank=False, upload_to='')
    school = models.ForeignKey(School, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_place'
        ordering = ['-id']

class PlaceFile(Period):
    file = models.ForeignKey(File, primary_key=True, on_delete=models.PROTECT, null=False)
    path = models.ImageField(null=False, blank=False, upload_to='place/%Y/%m/%d')

    class Meta:
        db_table = 'tbl_place_file'

class PlaceLike(Period):
    like = models.ForeignKey(Like, primary_key=True, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_place_like'

class PlacePoints(Period):
    points = models.ForeignKey(Point, primary_key=True, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_place_points'

class PlaceReview(Period):
    review = models.ForeignKey(Review, primary_key=True, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_place_review'