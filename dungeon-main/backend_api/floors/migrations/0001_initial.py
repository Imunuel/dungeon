from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dungeons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('position', models.PositiveIntegerField()),
                ('given_exp', models.PositiveIntegerField()),
                ('is_last', models.BooleanField()),
                ('dungeon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='floors', to='dungeons.dungeon')),
            ],
        ),
    ]