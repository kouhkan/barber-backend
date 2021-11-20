# Generated by Django 3.2 on 2021-11-19 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('barbers', '0003_auto_20211120_0009'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=5, verbose_name='Reserve Time')),
                ('date', models.DateField(verbose_name='Date')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('status', models.CharField(choices=[('r', 'Reserved'), ('a', 'Another Person'), ('c', 'Canceled'), ('f', 'Free')], default='a', max_length=1, verbose_name='Status')),
                ('barber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barber_reserve', to='barbers.barber')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reserve', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
