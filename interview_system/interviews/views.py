from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Interview
from datetime import datetime
from interviews.serializers import CreateModelSerializer, UpdateInterviewModelSerializer, listInterviewModelSerializer,\
    AnswerSerializer, InterviewSerializer, QuestionSerializer, OptionOfAnswerSerializer

from interviews.services import ParameterView


class UpdateInterviewView(generics.UpdateAPIView):
    def get_queryset(self):
        queryset = Interview.objects.all()
        return queryset

    serializer_class = UpdateInterviewModelSerializer


class UpdateView(ParameterView, generics.UpdateAPIView):
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = self._model.objects.all()
        return queryset

    """
    Api view для создания моделей
    """


class CreateView(ParameterView, generics.CreateAPIView):

    # permission_classes = [IsAdminUser]
    """
    Api view для создания моделей
    """


class DestroyAnswerView(generics.DestroyAPIView):
    # permission_classes = [IsAdminUser]
    serializer_class = AnswerSerializer


class DestroyInterviewView(generics.DestroyAPIView):
    # permission_classes = [IsAdminUser]
    serializer_class = InterviewSerializer


class DestroyQuestionView(generics.DestroyAPIView):
    # permission_classes = [IsAdminUser]
    serializer_class = QuestionSerializer


class DestroyOptionOfAnswerView(generics.DestroyAPIView):
    # permission_classes = [IsAdminUser]
    serializer_class = OptionOfAnswerSerializer


class CreateAnswerView(generics.CreateAPIView):
    # permission_classes = [IsAdminUser]
    serializer_class = AnswerSerializer


class CreateInterviewView(generics.CreateAPIView):
    # permission_classes = [IsAdminUser]
    serializer_class = InterviewSerializer


class CreateQuestionView(generics.CreateAPIView):
    # permission_classes = [IsAdminUser]
    serializer_class = QuestionSerializer


class CreateOptionOfAnswerView(generics.CreateAPIView):
    # permission_classes = [IsAdminUser]
    serializer_class = OptionOfAnswerSerializer


class ListView(ParameterView, generics.ListAPIView):
    """
    Api view для просмотра моделей
    """
    # permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        CreateModelSerializer.Meta.model = self._model
        return CreateModelSerializer

    def get_queryset(self):
        """
        Фильтрация по id пользователя
        """
        queryset = self._model.objects.all()
        return queryset


class ListInterviewView(generics.ListAPIView):
    serializer_class = listInterviewModelSerializer

    def get_queryset(self):
        queryset = Interview.objects

        queryset = queryset.filter(date_of_start__lte=datetime.now(), date_of_end__gte=datetime.now())

        return queryset

