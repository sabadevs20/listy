# Generated by Django 3.2.5 on 2021-07-12 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sell', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userz', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
