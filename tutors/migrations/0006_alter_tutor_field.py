# Generated by Django 3.2.5 on 2021-07-18 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0005_alter_tutor_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='field',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]