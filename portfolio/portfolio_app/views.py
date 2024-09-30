from rest_framework.response import Response
from rest_framework import status
from .models import (
    Projects,
    WorkExperience,
    Education,
    Review,
    Picture,
)
from .serializers import (
    ProjectSerializer,
    WorkExperienceSerializer,
    EducationSerializer,
    ReviewSerializer,
    PictureSerializer,
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
