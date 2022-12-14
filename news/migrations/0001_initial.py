# Generated by Django 4.1 on 2022-08-31 08:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='enter nick name here ...', max_length=100)),
                ('status', models.CharField(choices=[('Draft', 'DRAFT'), ('Public', 'PUBLIC')], db_index=True, default='STATUS', max_length=10)),
                ('content', django_ckeditor_5.fields.CKEditor5Field(blank=True, help_text='News Here ', null=True, verbose_name='Contents')),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('schedule_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Authors', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='favourite', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
