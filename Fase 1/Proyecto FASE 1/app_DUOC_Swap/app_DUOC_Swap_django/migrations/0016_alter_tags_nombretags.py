# Generated by Django 4.2.1 on 2023-06-08 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_DUOC_Swap_django', '0015_tags_categoriatags_delete_matchpublicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='nombreTags',
            field=models.CharField(max_length=90),
        ),
    ]
