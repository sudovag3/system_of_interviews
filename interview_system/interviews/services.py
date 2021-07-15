from django.views.decorators.csrf import csrf_exempt

from .models import Interview, Question, OptionOfAnswer, Answer, User
from .serializers import CreateModelSerializer
from django.http import JsonResponse

CT_MODEL_MODEL_CLASS = {
    'interview': Interview,
    'question': Question,
    'variant': OptionOfAnswer,
    'answer': Answer
}


class ParameterView:
    def dispatch(self, request, *args, **kwargs):
        self._model = CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        return super().dispatch(request, *args, **kwargs)

    def get_serializer_class(self):
        CreateModelSerializer.Meta.model = self._model
        return CreateModelSerializer


def create_answer(user, question, answer):
    """
    Функция создания ответа в базе
    :param user:
    :param question:
    :param answer:
    :return: JsonResponse
    """
    Answer.objects.create(user=User.objects.get(id=user), question=Question.objects.get(id=question),
                          answer=answer).save()
    return JsonResponse({'status': 'success', 'message': ""}, status=200)


@csrf_exempt
def send_answer(request):
    """
    Функция ответа на вопрос
    :param request:
    :return: JsonResponse
    """
    user_id = request.POST.get('user_id')
    question_id = request.POST.get('question_id')
    answer = request.POST.get('answer')

    if Question.objects.get(id=question_id).type_of_answers == 1 and \
            not (Answer.objects.filter(user=user_id,
                                       question=question_id).exists()):
        return create_answer(user_id, question_id, answer)

    elif Question.objects.get(id=question_id).type_of_answers == 2 and \
            not (Answer.objects.filter(user=user_id,
                                       question=question_id).exists()) and \
            OptionOfAnswer.objects.filter(question=question_id,
                                          text=answer).exists():

        return create_answer(user_id, question_id, answer)

    elif Question.objects.get(id=question_id).type_of_answers == 3 and \
            not (Answer.objects.filter(user=user_id,
                                       question=question_id,
                                       answer=answer).exists()) and OptionOfAnswer.objects.filter(question=question_id,
                                                                                                  text=answer).exists():
        return create_answer(user_id, question_id, answer)

    else:
        return JsonResponse({'status': 'false', 'message': "Проверьте корректность введённых вами данных"}, status=500)


def detail_answers(request):
    """
    Функция получения получения пройденных пользователем опросов с детализацией по ответам
    :param request:
    :return: JsonResponse
    """
    user_id = request.GET.get('user_id')
    if User.objects.get(id=user_id):
        res = {}

        for answer in Answer.objects.filter(user=user_id):
            question = answer.question
            interview = question.interview
            if interview.name in res.keys():
                if question.text in res[interview.name].keys():
                    res[interview.name][question.text].append(answer.answer)
                else:
                    res[interview.name][question.text] = [answer.answer]
            else:
                res[interview.name] = {question.text: [answer.answer]}

        return JsonResponse(res)
    else:
        return JsonResponse({'status': 'false', 'message': "Проверьте корректность введённых вами данных"}, status=500)


def detail_interview(request):
    id = request.GET.get('id')
    res = {}
    for i in (Question.objects.filter(interview=id)):
        res[f'question {i.id}'] = i.text
        if OptionOfAnswer.objects.filter(question=i.id).exists():
            options = {}
            for y in OptionOfAnswer.objects.filter(question=i.id):
                options[y.id] = y.text
            res[f'options of {i.id} question'] = options

    return JsonResponse(res)
