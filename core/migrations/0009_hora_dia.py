# Generated by Django 4.2.2 on 2023-11-26 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_hora_day_alter_day_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='hora',
            name='dia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.day'),
        ),
    ]
