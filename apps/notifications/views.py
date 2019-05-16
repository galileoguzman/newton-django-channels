from django.shortcuts import render

from .models import Notification


# Create your views here.
def notifications_list(request):
	notifications = Notification.objects.all()[:5]
	return render(request,
		'notifications.html',{
		'notifications' : notifications
	})