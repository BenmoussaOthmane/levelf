# Generated by Django 2.1.7 on 2019-03-16 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('My_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='etud',
            name='school',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='My_app.School'),
            preserve_default=False,
        ),
    ]