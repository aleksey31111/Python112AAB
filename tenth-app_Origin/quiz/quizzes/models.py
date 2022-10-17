from django.db import models
import random

DIFF_CHOICES = (
    ('easy', 'легкий'),
    ('medium', 'средний'),
    ('hard', 'сложный'),
)


class Quiz(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название теста')
    topic = models.CharField(max_length=120, verbose_name='Тема')
    number_of_questions = models.IntegerField(verbose_name='Количество вопросов')
    time = models.IntegerField(help_text='Продолжительность тестирования в минутах', verbose_name='Длительность теста')
    required_score_to_pass = models.IntegerField(help_text='Требуемый балл в %', verbose_name="Бал для прохождения")
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES, verbose_name='Сложность')

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
