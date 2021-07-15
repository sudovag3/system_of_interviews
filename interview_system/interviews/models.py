from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Interview(models.Model):
    name = models.CharField('Название опроса', max_length=255)
    date_of_start = models.DateTimeField('Дата начала опроса')
    date_of_end = models.DateTimeField('Дата окончания опроса')
    description = models.CharField('Описание опроса', max_length=1023)

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


# Create your models here.


class Question(models.Model):
    interview = models.ForeignKey(Interview, models.CASCADE, 'Опрос')
    text = models.CharField('Текст вопроса', max_length=1023)
    type_of_answers = models.PositiveIntegerField('Тип ответа', default=1)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class OptionOfAnswer(models.Model):

    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    text = models.CharField('Текст варианта', max_length=255)

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'


class Answer(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    question = models.ForeignKey(Question, models.CASCADE)
    answer = models.CharField('Текст Ответа', max_length=1023)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
