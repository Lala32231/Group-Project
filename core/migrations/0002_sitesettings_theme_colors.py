from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='theme_bg',
            field=models.CharField(default='#0f1117', max_length=7),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='theme_bg_2',
            field=models.CharField(default='#171a24', max_length=7),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='theme_accent',
            field=models.CharField(default='#ff8a4c', max_length=7),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='theme_accent_2',
            field=models.CharField(default='#6ea8fe', max_length=7),
        ),
    ]
