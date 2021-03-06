# Generated by Django 3.1.4 on 2020-12-10 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dboy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=20)),
                ('status', models.CharField(choices=[('ASD', 'assigned'), ('FRE', 'free')], db_column='dboy_st', default='FRE', max_length=5)),
                ('kms', models.FloatField(db_column='kms', default=0.0)),
                ('dailyDrivingTime', models.FloatField(db_column='dailyDrivingTime', default=0.0)),
                ('totalDrivingTime', models.FloatField(db_column='totalDrivingTime', default=0.0)),
                ('earnings', models.FloatField(db_column='earnings', default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(db_column='order_id', primary_key=True, serialize=False)),
                ('owner', models.CharField(db_column='owner', max_length=20)),
                ('lattitude', models.FloatField(db_column='lattitude')),
                ('longitude', models.FloatField(db_column='longitude')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('order_st', models.CharField(choices=[('RCD', 'rcvd'), ('ASD', 'dboy_asngd'), ('PKD', 'odr_pkd'), ('DLD', 'dlvrd')], db_column='order_st', max_length=5)),
                ('updated', models.DateTimeField(auto_now=True, db_column='updated')),
                ('payment_st', models.BooleanField(db_column='payment_st', default=False)),
                ('amt', models.FloatField(db_column='amt', default=0.0)),
                ('dboy_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dboy', to='core.dboy')),
            ],
        ),
    ]
