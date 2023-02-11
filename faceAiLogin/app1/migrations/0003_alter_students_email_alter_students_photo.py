# Generated by Django 4.1.6 on 2023-02-10 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_students_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='students',
            name='photo',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
