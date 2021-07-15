from django.urls import path
from django.views.generic import TemplateView
from interviews.views import *
from interviews.services import send_answer, detail_interview, detail_answers

from rest_framework.schemas import get_schema_view
urlpatterns = [
    path('update/interview/<int:pk>', UpdateInterviewView.as_view()),
    path('update/<str:ct_model>/<int:pk>', UpdateView.as_view()),
    path('create/answer', CreateAnswerView.as_view()),
    path('create/question', CreateQuestionView.as_view()),
    path('create/interview', CreateInterviewView.as_view()),
    path('create/option_of_answer', CreateOptionOfAnswerView.as_view()),
    path('destroy/answer', DestroyAnswerView.as_view()),
    path('destroy/question', DestroyQuestionView.as_view()),
    path('destroy/interview', DestroyInterviewView.as_view()),
    path('destroy/option_of_answer', DestroyOptionOfAnswerView.as_view()),
    path('open_interviews', ListInterviewView.as_view()),
    path('detail_interview', detail_interview),
    path('answer', send_answer),
    path('detail_answers', detail_answers),
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='redoc'),
    path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),

]
