from django.views.generic import TemplateView
from home.forms import HomeForm
from django.shortcuts import render, redirect
from home.models import Post

class HomeView(TemplateView):
	template_name = 'home/home.html'
	
	def get(self, request):
		form = HomeForm()
		posts = Post.objects.all()
		
		args = {'form':form, 'posts': posts}
		return render(request, self.template_name, args)
		
	def post(self, request):
		form = HomeForm(request.POST)
		if form.is_valid():
			# Clean the data to avoid SQL injection
			post = form.save(commit = False)
			post.user = request.user
			post.save()
			
			# Redirect so that the form will be cleared
			form = HomeForm()
			return redirect('home:home')
			
		args = {'form': form, 'text': text}
		return render(request, self.template_name, args)