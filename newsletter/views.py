from django.shortcuts import render
from .forms import ContactForm, SignUpForm
# Create your views here.
def home(request):	
	#Adds context to home.html, adds variable into template
	title = 'Welcome'
	if request.user.is_authenticated():
		title = "My Title %s" %(request.user)
	#if request.method == "POST":
		#print request.POST
	#render combines the request with it's arguments to make a more rich HTML file
	#context is a dict
	#
	form = SignUpForm(request.POST or None)
	context = { 
		"template_title": title,
		"form":  form,
	}

	if form.is_valid():
		instance = form.save(commit=False)
		#Pulls cleaned data and sets it to variable
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			instance.full_name = "Name N/A"	
		instance.save()
		context = {
			"template_title": "Thank You"
		}	


	return render(request, "home.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		#email = form.cleaned_data.get("email")
		#full_name = form.cleaned_data.get("full_name")
		#message = form.cleaned_data.get("message")
		#print full_name, email, message
		for key, value in form.cleaned_data.iteritems():
			print key + ": " + value
			#print form.cleaned_data.get(key)	
	context ={
		"form": form,
	}
	return render(request, "forms.html", context)
