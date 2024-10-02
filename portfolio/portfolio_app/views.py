from rest_framework.response import Response
from rest_framework import status
from rest_framework.schemas.coreapi import serializers
from .models import (
    Projects,
    WorkExperience,
    Education,
    Review,
    Picture,
    Articles,
    Contact,
)
from .serializers import (
    ProjectSerializer,
    WorkExperienceSerializer,
    EducationSerializer,
    ReviewSerializer,
    PictureSerializer,
    ArticleSerializer,
    ContactSerializer,
)
from rest_framework.views import APIView


class PictureView(APIView):
    def get(self, request):
        image = Picture.objects.all()
        serializer = PictureSerializer(image, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectView(APIView):
    def get(self, request):
        project = Projects.objects.all()
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WorkExperienceView(APIView):
    def get(self, request):
        work = WorkExperience.objects.all()
        serializer = WorkExperienceSerializer(work, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EducationView(APIView):
    def get(self, request):
        eduction = Education.objects.all()
        serializer = EducationSerializer(eduction, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReviewView(APIView):
    def get(self, request):
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectViewFor(APIView):
    def get(self, request, pk):
        project = Projects.objects.get(id=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticleView(APIView):
    def get(self, request):
        articles = Articles.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticleViewFor(APIView):
    def get(self, request, pk):
        article = Articles.objects.get(id=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ContactView(APIView):
    def get(self, request):
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"get the data"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
