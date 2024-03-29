# Generated by Django 2.2.1 on 2019-06-01 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('ticker', models.CharField(max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('open', models.DecimalField(decimal_places=2, max_digits=7)),
                ('close', models.DecimalField(decimal_places=2, max_digits=7)),
                ('high', models.DecimalField(decimal_places=2, max_digits=7)),
                ('low', models.DecimalField(decimal_places=2, max_digits=7)),
                ('volume', models.IntegerField(blank=True, null=True)),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Stock')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('resistance', models.DecimalField(decimal_places=2, max_digits=7)),
                ('support', models.DecimalField(decimal_places=2, max_digits=7)),
                ('stock_range', models.CharField(max_length=50)),
                ('comments', models.CharField(blank=True, max_length=1000, null=True)),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Stock')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
