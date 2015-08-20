from django.contrib import admin

from .models import Choice, Question

# Register your models here.

# admin.site.register(Question)

#This basically does the same thing as the registration above but this reorders the pub_date and question_text. Comes in handy when there are many different admin forms where the order needs to be intuitive.
# class QuestionAdmin(admin.ModelAdmin):
# 		fields = ['pub_date', 'question_text']

# admin.site.register(Question, QuestionAdmin)

#Or this one that creates fieldsets for the Question:
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]

# admin.site.register(Question, QuestionAdmin)

#Or this one that creates fieldsets and also initially displays the related fieldset with a class of 'collapse'.
# class QuestionAdmin(admin.ModelAdmin):
# 		fieldsets = [
# 				(None,					{'fields': ['question_text']}),
# 				('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
# 		]

# admin.site.register(Question, QuestionAdmin)

#But now we need to register Choice which is easy to do. We could go back to the top of the document and import Choice with Question. I'll just do that now.

# admin.site.register(Choice)

#The above is an inefficient way to add choices to questions. We can do it a different way. This will give us editable Choice objects on the Question admin page.

class ChoiceInline(admin.TabularInline):
		model = Choice
		extra = 3

class QuestionAdmin(admin.ModelAdmin):
		fieldsets = [
				(None,					{'fields': ['question_text']}),
				('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
		]
		inlines = [ChoiceInline]
		list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)

