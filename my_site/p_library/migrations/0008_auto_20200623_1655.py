# Generated by Django 3.0.7 on 2020-06-23 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0007_auto_20200623_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='isbn',
            new_name='ISBN',
        ),
    ]
