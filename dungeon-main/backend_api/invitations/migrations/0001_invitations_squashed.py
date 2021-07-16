# Generated by Django 3.2.4 on 2021-06-16 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('modified', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Modified at')),
                ('commentary', models.CharField(max_length=255, null=True, verbose_name='Invitation message')),
                ('status', models.IntegerField(choices=[(1, 'pending'), (2, 'approved'), (3, 'declined')], default=1, verbose_name='Invitation state')),
                ('invitee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_invites', to=settings.AUTH_USER_MODEL, verbose_name='Invitation receiver')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_invites', to=settings.AUTH_USER_MODEL, verbose_name='Invitation sender')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
