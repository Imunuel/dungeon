# Generated by Django 3.2.4 on 2021-06-11 12:08

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
            name='Dialog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
                ('text', models.TextField(verbose_name='Message text')),
                ('is_read', models.BooleanField(default=False, verbose_name='Read')),
                ('dialog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.dialog')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Messages',
                'ordering': ('datetime',),
            },
        ),
        migrations.CreateModel(
            name='DialogUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dialog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.dialog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='dialog',
            name='users',
            field=models.ManyToManyField(through='chat.DialogUser', to=settings.AUTH_USER_MODEL),
        ),
    ]