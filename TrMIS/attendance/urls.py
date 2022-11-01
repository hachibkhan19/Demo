from django.urls import path
from . import views

urlpatterns = [
    path('', views.ParentView.as_view()),
    path('post/<int:id>', views.detail_post_view, name='de')
]

