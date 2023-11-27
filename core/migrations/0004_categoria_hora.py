# Generated by Django 4.2.2 on 2023-11-25 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_comentarioperfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Hora',
            fields=[
                ('correlativo', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.TextField()),
                ('detalle', models.TextField()),
                ('nivel', models.TextField(choices=[('001', '08:00 - 08:45'), ('002', '08:45 - 09:30'), ('003', '09:30 - 10:15'), ('004', '10:15 - 11:00'), ('005', '11:00 - 11:45'), ('006', '11:45 - 12:30'), ('007', '12:30 - 13:15'), ('008', '13:15 - 14:00'), ('009', '14:00 - 14:45'), ('010', '14:45 - 15:30'), ('011', '15:30 - 16:15'), ('012', '16:15 - 17:00'), ('013', '17:00 - 17:45'), ('014', '17:45 - 18:30'), ('015', '18:30 - 19:15'), ('016', '19:15 - 20:00')])),
                ('fecha_envio', models.DateTimeField(auto_now_add=True)),
                ('fecha_ultima_modificacion', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
                ('publicado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
