from turtle import title
from django.contrib import admin

from app.models import JobPost

class JobAdmin(admin.ModelAdmin):
  list_display = ('company','title','salary', 'post_date',)
  list_filter = ('post_date','company','title','salary', 'expiry',)
  search_fields = ['title', 'company', 'salary',]
  search_help_text = "Search the title, company, or salary fields"
  exclude = ('post_date', 'slug')
  fieldsets = [
    (
      'Basic Information', 
      {
          "fields": ['title', 'description'],
      },
    ),
    (
      'More Information', 
      {
          'classes': ['collapse',],
          'fields': ['company','salary','expiry',]
      },
    ),
  ]

# Register your models here.
admin.site.register(JobPost, JobAdmin)