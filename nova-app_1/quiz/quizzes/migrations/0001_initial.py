# Generated by Django 4.0.5 on 2024-08-03 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Название теста')),
                ('topic', models.CharField(max_length=120, verbose_name='Тема')),
                ('number_of_questions', models.IntegerField(verbose_name='Количество вопросов')),
                ('time', models.IntegerField(help_text='Продолжительность тестирования в минутах', verbose_name='Длительность теста')),
                ('required_score_to_pass', models.IntegerField(help_text='Требуемый балл в %', verbose_name='Бал для прохождения')),
                ('difficulty', models.CharField(choices=[('easy', 'легкий'), ('medium', 'средний'), ('hard', 'сложный')], max_length=6, verbose_name='Сложность')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
    ]