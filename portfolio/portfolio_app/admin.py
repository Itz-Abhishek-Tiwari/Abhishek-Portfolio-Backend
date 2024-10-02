from django.contrib import admin
from .models import (
    Projects,
    WorkExperience,
    Education,
    Review,
    Skills,
    Picture,
    Articles,
    Contact,
)

admin.site.register(Projects)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Review)
admin.site.register(Skills)
admin.site.register(Picture)
admin.site.register(Articles)
admin.site.register(Contact)
