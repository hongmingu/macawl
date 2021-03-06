# Generated by Django 2.0.10 on 2019-01-27 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('relation', '0001_initial'),
        ('object', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.PositiveSmallIntegerField(choices=[(1001, 'bridge'), (1002, 'sub_url_object_help'), (1003, 'sub_url_object_comment')], default=0)),
                ('checked', models.BooleanField(default=False)),
                ('uuid', models.CharField(default=None, max_length=34, null=True, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NoticeBridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('bridge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='relation.Bridge')),
                ('notice', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notice.Notice')),
            ],
        ),
        migrations.CreateModel(
            name='NoticeCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NoticeSubUrlObjectComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('notice', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notice.Notice')),
                ('sub_url_object_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.SubUrlObjectComment')),
            ],
        ),
        migrations.CreateModel(
            name='NoticeSubUrlObjectHelp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('notice', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notice.Notice')),
                ('sub_url_object_help', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.SubUrlObjectHelp')),
            ],
        ),
    ]
