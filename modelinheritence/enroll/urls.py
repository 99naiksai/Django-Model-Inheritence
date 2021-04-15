from django.urls import path
from . import views
urlpatterns = [
    path('stu/', views.student_form),
    path('tea/' , views.teacher_form)

]