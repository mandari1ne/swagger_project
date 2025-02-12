# Generated by Django 4.1.1 on 2025-01-30 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_film_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='actor',
            name='birth_year',
        ),
        migrations.RemoveField(
            model_name='film',
            name='name',
        ),
        migrations.RemoveField(
            model_name='film',
            name='price',
        ),
        migrations.RemoveField(
            model_name='film',
            name='release_year',
        ),
        migrations.AddField(
            model_name='actor',
            name='country_of_birth',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='actor',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='date_of_creation',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='film',
            name='title',
            field=models.CharField(default='trulala', max_length=50),
        ),
        migrations.AlterField(
            model_name='film',
            name='description',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='film',
            name='main_actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='films.actor'),
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='films.genre', to_field='name'),
        ),
    ]
