from multiprocessing import context
from django.shortcuts import redirect, render
from django.urls import reverse
from subscribe.forms import SubscribeForm

from subscribe.models import Subscribe
from . import utilities

# Create your views here.
def subscribe(request):
  subscribe_form = SubscribeForm()
  subscribe_error_empty={}
  if request.POST:
    subscribe_form = SubscribeForm(request.POST)
    if subscribe_form.is_valid():
      subscribe_form.save()
      return redirect(reverse('thank_you'))
  context={"form":subscribe_form, "subscribe_error_empty":subscribe_error_empty}
  return render(request, 'subscribe/subscribe.html', context)

def thank_you(request):
  context = {}
  return render(request, 'subscribe/thank_you.html', context)
