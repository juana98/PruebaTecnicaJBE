# Generated by Django 3.2.5 on 2021-07-26 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DestLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_dest', models.IntegerField()),
                ('y_dest', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('last_update', models.DateTimeField(verbose_name='last-update')),
            ],
        ),
        migrations.CreateModel(
            name='PickupLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_pickup', models.IntegerField()),
                ('y_pickup', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('dest_location', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.destlocation')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.driver')),
                ('pickup_location', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.pickuplocation')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]