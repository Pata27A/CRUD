from django.urls import path
from .views import home_view, create_task_view, detail_task_view, crate_form_task_view
urlpatterns = [
    path('', home_view, name='home-view'),
    path('crear/', create_task_view, name='create_task'),
    path('tarea/<int:pk>/', detail_task_view, name='detail_task'),
    path('form_crear/', crate_form_task_view, name='crate_form_task_view')
]
