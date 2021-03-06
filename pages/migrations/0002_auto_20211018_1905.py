# Generated by Django 3.2.8 on 2021-10-18 19:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('asunto', models.CharField(max_length=100)),
                ('mensaje', models.TextField(blank=True)),
                ('is_answered', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='proyectos',
            name='activa',
            field=models.BooleanField(default=True, verbose_name='Página Activa'),
        ),
    ]
