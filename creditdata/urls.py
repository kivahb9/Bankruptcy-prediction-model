from django.urls import path
from creditdata import views

app_name = "credit"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("indexsquare/", views.indexsquare, name="indexsquare"),
    path("indexcube/", views.indexcube, name="indexcube"),

]
