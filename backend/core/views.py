from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .serializers import ProjectSerializer
from .serializers import RegisterSerializer
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .models import Prompt, Project
from .serializers import PromptSerializer
from django.conf import settings
import openai   
from .models import Project, Prompt, ChatMessage
from .serializers import ChatInputSerializer
from rest_framework.permissions import IsAuthenticated
from openai import OpenAI



class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered"}, status=201)
        return Response(serializer.errors, status=400)


class ProjectListCreateView(ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProjectDetailView(RetrieveAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)



class PromptListCreateView(ListCreateAPIView):
    serializer_class = PromptSerializer
    permission_classes = [IsAuthenticated]

    def get_project(self):
        project = get_object_or_404(Project, id=self.kwargs['project_id'])
        if project.user != self.request.user:
            raise PermissionDenied("Not your project")
        return project

    def get_queryset(self):
        project = self.get_project()
        return Prompt.objects.filter(project=project)

    def perform_create(self, serializer):
        project = self.get_project()
        serializer.save(project=project)

class ChatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, project_id):
        serializer = ChatInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_message = serializer.validated_data["message"]

        # Ownership check
        project = get_object_or_404(Project, id=project_id)
        if project.user != request.user:
            raise PermissionDenied("Not your project")

        # Build system prompt from stored prompts
        prompts = Prompt.objects.filter(project=project)
        system_prompt = "\n".join(
            [p.content for p in prompts]
        ) or "You are a helpful assistant."

        # Save user message
        ChatMessage.objects.create(
            project=project,
            role="user",
            content=user_message,
        )

        # OpenAI client
        client = OpenAI(api_key=settings.OPENAI_API_KEY)

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_message,
                },
            ],
        )

        assistant_reply = response.output_text

        # Save assistant reply
        ChatMessage.objects.create(
            project=project,
            role="assistant",
            content=assistant_reply,
        )

        return Response(
            {"reply": assistant_reply},
            status=status.HTTP_200_OK,
        )
