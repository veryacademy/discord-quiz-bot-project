from django.contrib import admin
from django.urls import path
from .quiz.views import RandomQuestion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/random/', RandomQuestion.as_view(), name='random'),
]
