# Generated by Django 2.0 on 2020-10-24 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_common_tad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='common_tad',
            name='coef_bioaccum_product',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='common_tad',
            name='lc50_c_product',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='common_tad',
            name='lc50_d_product',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='common_tad',
            name='ld50_product',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
