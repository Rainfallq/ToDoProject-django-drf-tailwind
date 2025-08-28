from django.urls import path, include
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, SignUpView, TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', TaskListView.as_view(), name = 'task_list'),
    path('add/', TaskCreateView.as_view(), name = 'task_create'),
    path('edit/<int:pk>/', TaskUpdateView.as_view(), name = 'task_update'),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name = 'task_delete'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]