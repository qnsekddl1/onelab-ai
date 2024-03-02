# Generated by Django 5.0.2 on 2024-03-03 01:25

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('onelab', '0001_initial'),
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneLabMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('onelab_member_status', models.SmallIntegerField(choices=[(0, '대기중'), (1, '참가'), (2, '거절'), (3, '탈퇴')], default=0)),
                ('onelab', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='onelab.onelab')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='university.university')),
            ],
            options={
                'db_table': 'tbl_onelab_member',
            },
        ),
    ]
