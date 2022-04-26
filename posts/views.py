from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from posts import serializers
from posts.models import *
from core.models import *
from posts.serializers import QuestionSerializer
# Create your views here.

class CreateQuestion(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            title=request.data.get("question")
            text=request.data.get("text")
            new_question = Question.objects.create(title=title, text=text, author=request.user)
            return Response({"message":f"New question created - id {new_question.id}"})
        else:
            return Response({"message":"Login to ask questions"})

class GetQuestion(APIView):
    def get(self, request, pk):
        serializer = QuestionSerializer(Question.objects.get(id=int(pk)))
        return Response(serializer.data)

class UpdateQuestion(APIView):
    def put(self, request, pk):
        question = Question.objects.get(id=int(pk))
        if question.author==request.user:
            title = request.data.get("title") or question.title
            text = request.data.get("text") or question.text
            question.save()
            serializer = QuestionSerializer(question)
            return Response(serializer)
        else:
            return Response({"message":"You are not authorized to edit this question."})

class DeleteQuestion(APIView):
    def delete(self, request, pk):
        question = Question.objects.get(id=int(pk))
        if question.author==request.user:
            question.delete()
            return Response({"message":"Deleted"})
        else:
            return Response({"message":"You are not authorized to delete this question."})

class CreateAnswer(APIView):
    def post(self, request, pk):
        question = Question.objects.get(id=int(pk))
        if request.user.is_authenticated:
            text=request.data.get("text")
            new_answer = Answer.objects.create(text=text, author=request.user, question_object=question)
            return Response({"message":f"New answer created - id {new_answer.id}"})
        else:
            return Response({"message":"Login to answer questions"})