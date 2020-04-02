# Generated by Django 3.0.3 on 2020-03-30 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pandaid_base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='need',
            name='items',
            field=models.ManyToManyField(through='pandaid_base.ItemNeed', to='pandaid_base.Item'),
        ),
        migrations.RemoveField(
            model_name='itemneed',
            name='item',
        ),
        migrations.AddField(
            model_name='itemneed',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pandaid_base.Item'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='itemneed',
            name='need',
        ),
        migrations.AddField(
            model_name='itemneed',
            name='need',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pandaid_base.Need'),
            preserve_default=False,
        ),
    ]