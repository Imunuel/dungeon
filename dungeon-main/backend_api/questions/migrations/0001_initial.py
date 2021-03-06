# Generated by Django 3.2.4 on 2021-06-15 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('right_answer', models.CharField(max_length=255)),
            ],
            options={
                'default_related_name': 'questions',
            },
        ),
    ]
