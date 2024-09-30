from django.urls import path
from .views import (
    ProjectView,
    WorkExperienceView,
    EducationView,
    ReviewView,
    ProjectViewFor,
    PictureView,
)

urlpatterns = [
    # Get full Data
    path("projects/", ProjectView.as_view(), name="projects"),
    path("work/", WorkExperienceView.as_view(), name="works"),
    path("education/", EducationView.as_view(), name="educations"),
    path("review/", ReviewView.as_view(), name="reviews"),
    path("pictures/", PictureView.as_view(), name="picture"),
    #
    # Get data per ID
    path("projects/<int:pk>", ProjectViewFor.as_view(), name="project"),
    path("work/<int:pk>", WorkExperienceView.as_view(), name="work"),
    path("education/<int:pk>", EducationView.as_view(), name="education"),
    path("review/<int:pk>", ReviewView.as_view(), name="review"),
]
