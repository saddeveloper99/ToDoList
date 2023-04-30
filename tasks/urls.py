from django.urls import path
from tasks.views import TaskView, TaskDetailView


urlpatterns = [
    path("", TaskView.as_view(), name="task_view"),
    path("detail/<int:task_id>/", TaskDetailView.as_view(), name="tasklist_view"),
]
