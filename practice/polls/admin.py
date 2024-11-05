from django.contrib import admin
from .models import Question, Choice ,dummy


# Register your models here.
# admin.site.register(Question)
# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class dummyline(admin.TabularInline):
    model = dummy
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields': ['question_text']})]

    inlines = [ChoiceInline,dummyline]



admin.site.register(Question,QuestionAdmin)

# admin.site.register(dummy)