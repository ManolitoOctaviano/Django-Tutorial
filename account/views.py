from django.shortcuts import render, redirect
from account.forms import RegistrationForm, EditProfileForm

# Use to get the login user. See: view_profile()
from django.contrib.auth.models import User
# Use to edit the information. See: edit_profile()
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
# Use to make the user still login after changing password
from django.contrib.auth import update_session_auth_hash

# Use to restrict guest user on going to specific urls (or use the middleware.py)
# Example:
#     @login_required
#	  def method1():
from django.contrib.auth.decorators import login_required


	
def register(request):
	if request.method == 'POST':
		# Check the form.py for the details
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')
	else:
		form = RegistrationForm()
		
		args = {'form': form}
		return render(request, 'account/reg_form.html', args)

# Gets the user of the login account
def view_profile(request, pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user = request.user
	args = {'user': user}
	return render(request, 'account/profile.html', args)
	

def edit_profile(request):
	if request.method == 'POST':
		# Check the form.py for the details
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('/account/profile')
	else:
		form = EditProfileForm(instance=request.user)
		args= {'form':form}
		return render(request, 'account/edit_profile.html', args)


def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			# Making sure that the user is still login even after changing the password
			update_session_auth_hash(request, form.user)
			return redirect('/account/profile')
	else:
		form = PasswordChangeForm(user=request.user)
		args= {'form':form}
		return render(request, 'account/change_password.html', args)