from django.contrib import admin
from .models import UserProfile

# Register your models here.
#admin.site.register(UserProfile)

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'user_info', 'phone_num')
	
	def user_info(self, object):
		return object.description
	
	def phone_num(self, object):
		return object.phone
		
	def get_queryset(self, request):
		queryset = super(UserProfileAdmin, self).get_queryset(request)
		queryset = queryset.order_by('-phone', 'user')
		
		return queryset
		
admin.site.register(UserProfile, UserProfileAdmin)