# Generated by Django 3.1.1 on 2021-11-19 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211119_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.BigAutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, max_length=11, unique=True, verbose_name='Phone Number'),
        ),
    ]