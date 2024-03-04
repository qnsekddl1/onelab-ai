from django.test import TestCase

from school.models import School


class schoolTests(TestCase):
    school = School.objects.create(
        member_id=6,
        school_member_address='서울특별시 관악구 관악로 1',
        school_name='서울대학교',
    )