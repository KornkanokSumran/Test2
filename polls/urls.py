from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('delete/', views.remove.as_view(), name='delete'),
    path('input/', views.input, name='input'),
    path('show/', views.show, name='show'),
    path('delete_question/', views.delete_question, name='delete_question'),
    path('table/', views.table.as_view(), name='table'),
    path('css/', views.css, name='column'),
]