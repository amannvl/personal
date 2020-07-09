# Generated by Django 3.0.8 on 2020-07-09 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('subject', models.CharField(default='', max_length=150)),
                ('message', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(default='', null=True)),
                ('github_url', models.URLField(blank=True, default='', null=True)),
                ('desc', models.TextField(default='', null=True)),
                ('language', models.CharField(default='', max_length=150, null=True)),
                ('framework', models.CharField(default='', max_length=250)),
                ('client', models.CharField(default='', max_length=250)),
                ('date', models.CharField(default='', max_length=100)),
                ('keyword', models.CharField(default='', max_length=350, null=True)),
                ('subtitle', models.CharField(default='', max_length=300)),
                ('web_url', models.URLField(blank=True, default='', null=True)),
                ('image_url', models.ImageField(blank=True, default='', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(default='', max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=500, null=True)),
                ('subtitle', models.TextField(blank=True, default='', null=True)),
                ('specialmsg', models.TextField(blank=True, default='', null=True)),
                ('referral_url', models.URLField(blank=True, default='', null=True)),
                ('desc', models.TextField(default='', null=True)),
                ('category', models.CharField(default='', max_length=150, null=True)),
                ('date', models.DateTimeField(blank=True)),
                ('keyword', models.CharField(default='', max_length=350, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Blogs')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.BlogComment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
