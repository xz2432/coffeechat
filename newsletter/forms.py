from django import forms

from .models import SignUp
class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']
	

	#form validation
	def clean_email(self):
		#cleans up email input and returns clean email
		
		email = self.cleaned_data.get('email')
		#Checks for .edu extension
		email_base, provider = email.split("@")
		domain, extension = provider.split(".")
		if not extension == "edu":
			raise forms.ValidationError("Please use a valid .EDU college email address")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get("full_name")
		return full_name
