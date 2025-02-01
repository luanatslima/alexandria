# Generated by Django 5.1.5 on 2025-02-01 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=100, unique=True)),
                ('descricao', models.TextField(max_length=100)),
                ('titulo', models.CharField(max_length=200)),
                ('tipo', models.CharField(choices=[('SL', 'Slide'), ('VD', 'Vídeo'), ('DC', 'Documento')], default='DC', max_length=2)),
                ('arquivo', models.FileField(upload_to='meus_materiais/')),
            ],
        ),
    ]
