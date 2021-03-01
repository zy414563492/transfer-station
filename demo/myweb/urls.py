from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]

app_name = 'myweb'

# urlpatterns = [
#     # ex: /myweb/
#     path('', views.index, name='index'),
#     # ex: /myweb/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /myweb/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /myweb/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
