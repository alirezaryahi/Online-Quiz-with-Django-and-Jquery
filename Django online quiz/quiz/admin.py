from django.contrib import admin
from quiz.models import Quiz


# Register your models here.


class QuizAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']

    class Meta:
        model = Quiz


admin.site.register(Quiz, QuizAdmin)
