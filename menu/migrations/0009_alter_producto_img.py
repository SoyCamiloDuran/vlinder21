# Generated by Django 4.1.6 on 2023-03-17 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_alter_producto_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='img',
            field=models.ImageField(default='../../static/img/logovlinder.jpg', upload_to='../../static/img/img-producto'),
        ),
    ]