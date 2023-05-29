from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

job_title = [
  "First Job", "Second Job", "Third Job", 
]

job_description = [
  "First Job Description", "Second Job Description", "Third Job Description"
]

def job_list(request):
  # display list of jobs
  list_page = "<ul>"
  for idx, title in enumerate(job_title):
    detail_url = reverse('job_detail', args=(idx,))
    list_page += f"<li><h3><a href='{detail_url}'>{title}</a></h3></li>"
  list_page += "</ul>"
  return HttpResponse(list_page)

def job_detail(request, id):
  try:
    if(id == 8000):
      return redirect(reverse('job_home'))
    return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
    return HttpResponse(return_html)
  except Exception:
    return HttpResponseNotFound("Not Found")
