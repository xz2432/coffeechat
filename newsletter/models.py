from django.db import models

# Create your models here.
class SignUp(models.Model):
	full_name = models.CharField(max_length=100, blank=False, null=True)
	email = models.EmailField(max_length=100, blank=False, null=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.email
