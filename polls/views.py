
import abc
from re import template
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect, response
from django.template import loader
from rest_framework.serializers import Serializer
from .models import Question, Choice
from django.urls import reverse 
from django.views import generic
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import QuestionSerializer

#from .models import LopSample # LopSample 모델 불러오기

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        #return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    

'''
def index(request):
    #1
    #return HttpResponse("Hello, world. You're at the polls index.")
    
    #2 
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    
    #3
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list' : latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    
    #4
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'polls/index.html', context)

# def lop_sample_view(request):
#     lopsamples = LopSample.objects.all() # LopSample 테이블의 모든 객체 불러와서 lop_sample_view에 저장
#     return render(request, 'index.html', {"lopsamples":lopsamples})

def detail(request, question_id):
    #여기서 막 작업해도됨.
    # 1
    # return HttpResponse("You're looking at question %s." % question_id)
    
    # 2
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html',{'question':question})
    
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
'''

def vote(request, question_id):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # not data
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # Post로 View가 열리면 HttpResponseRedirect로 return 둘이 한세트임
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class QuestionListAPIView(APIView):
    def get(self, request):
        serializer = QuestionSerializer(Question.objects.all(), many=True)
        #question = self.get_object(pk=pk)
        #serializer = QuestionSerializer(question)
        return Response(serializer.data)
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class QuestionListDetailAPIView(APIView):
    def get(self, request, pk):
        question = get_object_or_404(Question, pk =pk)
        
        serializer = QuestionSerializer(question)
        return Response(serializer.data)