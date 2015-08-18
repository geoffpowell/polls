from django.contrib import admin

from .models import Question

# Register your models here.
# admin.site.register(Question)

#This basically does the same thing as the registration above but this reorders the pub_date and question_text. Comes in handy when there are many different admin forms where the order needs to be intuitive.
class QuestionAdmin(admin.ModelAdmin):
		fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)