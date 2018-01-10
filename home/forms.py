from django import forms
from home.models import Post

class HomeForm(forms.ModelForm):
	post = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Write a post...'
		}
	))
	
	# This is the model class that is created to save the data in form.
	class Meta:
		model = Post
		fields = ('post',)