from django.db.models import Q
from django.test import TestCase

from alarm.models import Alarm


class AlarmTestCase(TestCase):
    print(100000)
    alarm_objects = Alarm.objects.filter(
        (Q(alarm_receiver='김규산') | Q(member_id=2) & ~Q(alarm_status=-1))). \
                        values('onelab_id').order_by('-created_date')[0:5]
    print('='*20)
    print(alarm_objects)
    print('='*20)
    pass