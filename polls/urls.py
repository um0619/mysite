from re import template
from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'polls'
urlpatterns = [
    # 1 
    # # ex : /polls/
    # path('', views.index, name='index'),
    # #path('lop/', views.lop_sample_view),
    # #path('form-class-ex-thanks', TemplateView.as_view(template_name = "polls/"))
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex : /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex : /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', views.DetailView.as_view(), name= 'detail'),
    path('<int:pk>/result/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
