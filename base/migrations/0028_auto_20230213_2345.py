# Generated by Django 3.2.4 on 2023-02-13 18:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_auto_20230213_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_SECTION',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=2000)),
                ('Address', models.CharField(max_length=2000)),
                ('Phone_number', models.CharField(max_length=2000)),
                ('E_Mail', models.ImageField(default='carrer/Screenshot_3.png', upload_to='HOME_TESTIMONIAL/%Y/%m/%d')),
                ('updated_date', models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc))),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='angelinvestordb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='angelinvestorsdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='awards',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 270527, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='awards',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 279734, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='birac',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='carrer',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='centralgovernmentfundingdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='demodaydb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 270527, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='events',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 270527, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventsform',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 270527, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='globalmarketconnectdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='home_testimonial',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='latest_news',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='logo',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 270527, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mentorclinicdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mentorconnectdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mission',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 279734, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='new_venturesdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sisfs',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='stategovernmentfundingdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tbi',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='team',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 279734, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 279734, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='value',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='venturecapitalistdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vision',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 279734, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='whoarewe',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 15, 6, 280824, tzinfo=utc)),
        ),
    ]
