# Generated by Django 3.2.9 on 2021-12-07 23:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cometario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cometario', models.CharField(max_length=25)),
                ('email_comentario', models.EmailField(max_length=254)),
                ('comentario', models.TextField()),
                ('data_comentario', models.DateTimeField(default=django.utils.timezone.now)),
                ('publicado_comentario', models.BooleanField(default=False)),
            ],
        ),
    ]