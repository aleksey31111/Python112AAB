# Generated by Django 4.0.5 on 2022-10-17 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='Вопрос')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.quiz', verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='Вариант ответа')),
                ('correct', models.BooleanField(default=False, verbose_name='Правильный ответ')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.question', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
