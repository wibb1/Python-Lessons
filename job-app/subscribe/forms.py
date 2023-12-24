from wsgiref.validate import validator
from django import forms
from django.utils.translation import gettext_lazy as _
from subscribe.models import Subscribe

class SubscribeForm(forms.ModelForm):
  class Meta:
    model = Subscribe
    # fields=['first_name','last_name','email'] # when you want to select only certain ones
    # exclude={'first_name',} # allows you to exclude values from the form
    fields='__all__'
    labels={
      'first_name':_('Enter first name'),
      'last_name':_('Enter last name'),
      'email':_('Enter a valid email'),
    }
    help_texts={
      'first_name': _('Enter only characters')
    }
    error_messages={
      'first_name':{ 'required':_('First name is required') },
      'last_name':{ 'required':_('Last name is required') },
      'email':{ 'required':_('Enter a valid email') },
    }
    
# # Single variable validation inside of class
# def validate_comma(value):
#     if "," in value:
#       raise forms.ValidationError("Invalid Character Used")
#     return value
  
# # using just forms.Form and not ModelForm
# class SubscribeForm(forms.Form):
#   first_name = forms.CharField(
#     max_length=100, 
#     label='Enter first name', 
#     help_text='Enter your first name'
#   )
#   last_name = forms.CharField(
#     max_length=100, 
#     validators=[validate_comma], 
#     label='Enter last name', 
#     help_text='Enter your last name'
#   )
#   email = forms.EmailField(
#     max_length=100, 
#     help_text='Enter a valid email address', 
#     label='Enter your email address'
#   )

# # Multiple Variable validation - outside of class  
#   def clean_first_name(self):
#       data = self.cleaned_data["first_name"]
#       if "," in data:
#         raise forms.ValidationError("Invalid First Name")
#       return data
