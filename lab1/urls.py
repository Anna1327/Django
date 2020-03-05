from django.urls import path
from lab1.views import LoginView

urlpatterns = [
    path('', LoginView.as_view()),

]


#localhost:8000/lab1