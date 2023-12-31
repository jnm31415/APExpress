# Generated by Django 4.1.2 on 2023-04-20 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aufträge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auftragspositionen',
            name='referenz',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='auftrag',
            name='angenommen',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='auftrag',
            name='fahrer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Aufträge.fahrer'),
        ),
        migrations.AlterField(
            model_name='auftragspositionen',
            name='kostenstelle',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
