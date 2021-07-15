from rest_framework import serializers
from interviews.models import Answer, Question, Interview, OptionOfAnswer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'


class OptionOfAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionOfAnswer
        fields = '__all__'


class CreateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = '__all__'


class listInterviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'


class UpdateInterviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ['name', 'date_of_end', 'description']