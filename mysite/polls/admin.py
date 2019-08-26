from django.contrib import admin
from .models import Choice, Question


# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date')

     inlines = [ChoiceInline]


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
