from django.contrib import admin
from lessons.models import Lesson,Category

class LessonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Lesson,LessonAdmin)
admin.site.register(Category)
