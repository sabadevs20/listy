# Generated by Django 3.2.3 on 2021-07-19 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0006_remove_category_advert'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='advert',
            field=models.ManyToManyField(related_name='adverts', to='sell.Advert'),
        ),
    ]
