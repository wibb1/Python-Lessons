from dataclasses import fields
from os import name
from turtle import title
from django.contrib import admin

from app.models import JobPost, Location, Skill

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
    (
      'Location',
      {
        'classes': ['collapse'],
        'fields': ['location',]
      }
    ),
    (
      'Skills',
      {
        'classes': ['collapse'],
        'fields': ['name',]
      }
    )
  ]
  
class LocationAdmin(admin.ModelAdmin):
  fieldsets = [
    (
      'Location', 
      {
          'fields': ['street','city', 'state', 'country', ]
      },
    ),
  ]

class SkillAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Skill name', {'fields': ['name']})
  ]
  
# Register your models here.
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Skill)