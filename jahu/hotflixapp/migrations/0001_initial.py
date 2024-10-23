# Generated by Django 5.1.2 on 2024-10-22 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan_Receiver',
            fields=[
                ('rid', models.CharField(max_length=20, primary_key='rid', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('loan_amount', models.IntegerField()),
                ('dob', models.IntegerField()),
                ('receiver_referance', models.IntegerField()),
            ],
        ),
    ]
