# Generated by Django 4.0 on 2021-12-19 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('report', '0002_alter_reports_datepub'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='auth.user')),
            ],
        ),
    ]
