# Generated by Django 3.1.3 on 2020-11-11 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='actor',
            new_name='actors',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='director',
            new_name='directors',
        ),
    ]