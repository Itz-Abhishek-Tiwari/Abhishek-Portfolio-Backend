from rest_framework import serializers
from .models import Projects, WorkExperience, Education, Review, Skills, Picture


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    image = PictureSerializer(many=True)

    class Meta:
        model = Projects
        fields = [
            "id",
            "project_title",
            "project_description",
            "git_link",
            "skills",
            "image",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["skills"] = [
            skill.technologies for skill in instance.skills.all()
        ]
        return representation


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
