# Generated by Django 3.1.4 on 2020-12-12 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseHub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lang_tag', models.CharField(max_length=100)),
                ('module', models.BooleanField()),
                ('course_tag', models.CharField(max_length=100)),
                ('location_url', models.URLField()),
                ('rating', models.IntegerField(default=1)),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('rating',),
            },
        ),
    ]