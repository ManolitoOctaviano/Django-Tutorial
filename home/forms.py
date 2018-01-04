from django import forms
from home.models import Post

class HomeForm(forms.ModelForm):
	post = forms.CharField()
	
	# This is the model class that is created to save the data in form.
	class Meta:
		model = Post
		fields = ('post',)