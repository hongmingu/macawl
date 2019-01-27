# Generated by Django 2.0.10 on 2019-01-27 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=2048, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('keyword', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Keyword')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubRawKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=2048, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sub_keyword', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.SubKeyword')),
            ],
        ),
        migrations.CreateModel(
            name='SubRawKeywordCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveSmallIntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubUrlObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, default=None, max_length=34, null=True, unique=True)),
                ('help_count', models.PositiveIntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubUrlObjectComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=1000, null=True)),
                ('uuid', models.CharField(blank=True, default=None, max_length=34, null=True, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sub_url_object', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.SubUrlObject')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubUrlObjectCommentCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sub_url_object', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.SubUrlObject')),
            ],
        ),
        migrations.CreateModel(
            name='SubUrlObjectHelp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sub_url_object', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.SubUrlObject')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubUrlObjectInitialUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(blank=True, default=None, max_length=2060, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sub_url_object', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.SubUrlObject')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubUrlObjectSubKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sub_keyword', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.SubKeyword')),
                ('sub_url_object', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.SubUrlObject')),
            ],
        ),
        migrations.CreateModel(
            name='SubUrlObjectSubKeywordStart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up_count', models.PositiveIntegerField(default=0)),
                ('down_count', models.PositiveIntegerField(default=0)),
                ('register_count', models.PositiveIntegerField(default=0)),
                ('sub_url_object_sub_keyword', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.SubUrlObjectSubKeyword')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=1000, null=True)),
                ('status', models.CharField(blank=True, default='200', max_length=20, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UrlKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, default=None, max_length=34, null=True, unique=True)),
                ('up_count', models.PositiveIntegerField(default=0)),
                ('down_count', models.PositiveIntegerField(default=0)),
                ('register_count', models.PositiveIntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('keyword', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Keyword')),
            ],
        ),
        migrations.CreateModel(
            name='UrlKeywordDown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('url_keyword', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.UrlKeyword')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UrlKeywordRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('url_keyword', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.UrlKeyword')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UrlKeywordUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('url_keyword', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.UrlKeyword')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UrlObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc', models.TextField(blank=True, default=None, max_length=2050, null=True)),
                ('http', models.BooleanField(default=False)),
                ('https', models.BooleanField(default=False)),
                ('uuid', models.CharField(blank=True, default=None, max_length=34, null=True, unique=True)),
                ('is_discrete', models.BooleanField(default=False)),
                ('in_not_301', models.BooleanField(default=False)),
                ('discrete_loc', models.TextField(blank=True, default=None, max_length=2050, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='urlkeyword',
            name='url_object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.UrlObject'),
        ),
        migrations.AddField(
            model_name='title',
            name='url_object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.UrlObject'),
        ),
        migrations.AddField(
            model_name='suburlobject',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Title'),
        ),
        migrations.AddField(
            model_name='suburlobject',
            name='url_object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.UrlObject'),
        ),
        migrations.AddField(
            model_name='suburlobject',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subrawkeywordcount',
            name='sub_url_object',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.SubUrlObject'),
        ),
        migrations.AddField(
            model_name='subrawkeyword',
            name='sub_url_object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.SubUrlObject'),
        ),
        migrations.AddField(
            model_name='subrawkeyword',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='urlkeywordup',
            unique_together={('user', 'url_keyword')},
        ),
        migrations.AlterUniqueTogether(
            name='urlkeywordregister',
            unique_together={('user', 'url_keyword')},
        ),
        migrations.AlterUniqueTogether(
            name='urlkeyworddown',
            unique_together={('user', 'url_keyword')},
        ),
        migrations.AlterUniqueTogether(
            name='urlkeyword',
            unique_together={('url_object', 'keyword')},
        ),
        migrations.AlterUniqueTogether(
            name='suburlobjectsubkeyword',
            unique_together={('sub_url_object', 'sub_keyword')},
        ),
        migrations.AlterUniqueTogether(
            name='suburlobjecthelp',
            unique_together={('user', 'sub_url_object')},
        ),
        migrations.AlterUniqueTogether(
            name='suburlobject',
            unique_together={('user', 'url_object')},
        ),
        migrations.AlterUniqueTogether(
            name='subkeyword',
            unique_together={('user', 'keyword')},
        ),
    ]