from django.db import models


class Picture(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="uploads/")

    def __str__(self):
        return self.name


class Skills(models.Model):
    technologies = models.CharField(max_length=100)

    def __str__(self):
        return self.technologies


class Projects(models.Model):
    project_title = models.CharField(max_length=100)
    project_description = models.TextField(null=True, blank=True)
    git_link = models.URLField(null=True, blank=True)
    live_link = models.URLField(null=True)
    skills = models.ManyToManyField(Skills)
    image = models.ManyToManyField(Picture)

    def __str__(self):
        return self.project_title


class WorkExperience(models.Model):
    company = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return f"worked at {self.company}"


class Education(models.Model):
    institution = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    degree = models.CharField(
        max_length=100,
        null=True,
    )
    cgpa = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return f"Done {self.degree} from {self.institution}"


class Review(models.Model):
    feedback = models.TextField()
    professor = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"Review by {self.professor}"


class Articles(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ManyToManyField(Picture)
    link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
