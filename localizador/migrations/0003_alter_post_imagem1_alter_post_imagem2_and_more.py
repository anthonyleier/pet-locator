# Generated by Django 4.1.1 on 2022-09-23 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localizador', '0002_remove_post_autor_alter_post_imagem1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagem1',
            field=models.ImageField(blank=True, null=True, upload_to='localizador/upload/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagem2',
            field=models.ImageField(blank=True, null=True, upload_to='localizador/upload/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagem3',
            field=models.ImageField(blank=True, null=True, upload_to='localizador/upload/%Y/%m/%d/'),
        ),
    ]
