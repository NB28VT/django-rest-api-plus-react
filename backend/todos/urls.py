from django.conf.urls import url

from . import views

urlpatterns = [
    url("", views.ListTodo.as_view()),
    url("<int:pk>", views.DetailTodo.as_view())
]
