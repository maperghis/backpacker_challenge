# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=300, verbose_name=b'first name')),
                ('lastName', models.CharField(max_length=300, verbose_name=b'last name')),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(30)])),
                ('gender', models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('eyeColour', models.CharField(default=b'Br', max_length=2, verbose_name=b'eye colour', choices=[(b'Br', b'Brown'), (b'Bl', b'Blue')])),
                ('nationality', models.CharField(default=b'Br', max_length=2, choices=[(b'Br', b'British'), (b'Fr', b'French'), (b'Gr', b'German'), (b'Sp', b'Spanish'), (b'It', b'Italian'), (b'Sw', b'Swiss'), (b'Cn', b'Canadian')])),
                ('email', models.EmailField(max_length=254, verbose_name=b'email address')),
                ('phone', models.CharField(max_length=254, verbose_name=b'phone number', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'.Up to 15 digits allowed.")])),
                ('distance', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100000)])),
                ('days', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(720)])),
                ('working', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300, verbose_name=b'name of state or territory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mode', models.CharField(max_length=300, verbose_name=b'mode of transport')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='states',
            field=models.ManyToManyField(related_name=b'people_states', to='backpackers.State'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='transport',
            field=models.ManyToManyField(related_name=b'people_transports', to='backpackers.Transport'),
            preserve_default=True,
        ),
    ]
