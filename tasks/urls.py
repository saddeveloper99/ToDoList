from django.urls import path
from tasks.views import TaskCreateView


urlpatterns = [
    path("", TaskCreateView.as_view(), name="task_create_view"),
]
