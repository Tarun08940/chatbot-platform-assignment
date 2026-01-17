from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import (
    RegisterView,
    ProjectListCreateView,
    ProjectDetailView,
    PromptListCreateView,
    ChatView,
)

urlpatterns = [
    # Auth
    path("auth/register/", RegisterView.as_view()),
    path("auth/login/", TokenObtainPairView.as_view()),

    # Projects
    path("projects/", ProjectListCreateView.as_view()),
    path("projects/<int:pk>/", ProjectDetailView.as_view()),

    # Prompts
    path(
        "projects/<int:project_id>/prompts/",
        PromptListCreateView.as_view(),
    ),

    # Chat 
    path(
        "projects/<int:project_id>/chat/",
        ChatView.as_view(),
    ),
]
