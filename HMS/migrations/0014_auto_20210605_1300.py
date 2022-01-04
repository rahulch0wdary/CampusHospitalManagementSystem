# Generated by Django 3.2.4 on 2021-06-05 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0013_auto_20210605_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facultymedicine',
            name='appointment',
        ),
        migrations.RemoveField(
            model_name='studentmedicine',
            name='appointment',
        ),
        migrations.AddField(
            model_name='facultymedicine',
            name='treatment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='HMS.facultytreatment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentmedicine',
            name='treatment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='HMS.studenttreatment'),
            preserve_default=False,
        ),
    ]
