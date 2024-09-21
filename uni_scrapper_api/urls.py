# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='Hello'),
    path('university/', views.get_universities, name='List of universities'),
    path('university/<str:university_name>/', views.run_course_spider, name='course_spider'),
]
