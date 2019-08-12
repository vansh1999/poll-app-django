from django.urls import path

from . import views


app_name = 'polls'
urlpatterns = [
    # polls/home/
    path('home/' , views.index , name = "index"),
    # polls/details/3
    path('detail/<int:question_id>/', views.detail, name="detail"),
    # polls/results/3
    path('<int:question_id>/results/', views.results , name="results"),
    # polls/vote/3
    path('<int:question_id>/vote/', views.vote, name="vote"),

]

