from django.contrib import admin
from .models import Question
from .models import Answer

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
# QuestionAdmin, AnswerAdmin 은 검색 기능을 추가하기 위해 작성한 것 !!