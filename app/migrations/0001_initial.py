# Generated by Django 2.1.2 on 2018-10-20 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversion',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Raw', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Emoji',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Text', models.CharField(max_length=5)),
                ('Order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EmojiKeyword',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Keyword', models.CharField(max_length=250)),
                ('SuggestedByUser', models.BooleanField(default=False)),
                ('Emoji', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to= 'app.Emoji', verbose_name= 'Emoji')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Value', models.BooleanField(default=True)),
                ('Conversion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to= 'app.Conversion', verbose_name= 'Processed Tweet')),
            ],
        ),
        migrations.AddField(
            model_name='conversion',
            name='EmojiList',
            field=models.ManyToManyField(to= 'app.EmojiKeyword', verbose_name= 'Emoji List'),
        ),
    ]