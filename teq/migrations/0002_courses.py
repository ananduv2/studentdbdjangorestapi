# Generated by Django 3.2.3 on 2021-05-29 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('CourseId', models.AutoField(primary_key=True, serialize=False)),
                ('CourseName', models.CharField(max_length=100)),
                ('CourseRate', models.IntegerField()),
            ],
            options={
                'db_table': 'courses',
            },
        ),
    ]
