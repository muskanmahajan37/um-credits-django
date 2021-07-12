from django.urls import path

from .views import SubjectsView

urlpatterns = [
    path('add-subject/', SubjectsView.as_view()),

]
