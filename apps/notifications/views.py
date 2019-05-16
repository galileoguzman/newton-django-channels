from django.shortcuts import render
from rest_framework import viewsets

from .models import Notification
from .serializers import NotificationSerializer


# APP VIEWS.
def notifications_list(request):
	notifications = Notification.objects.all()[:5]
	return render(request,
		'notifications.html',{
		'notifications' : notifications
	})


# API VIEWS
class NotificationViewSet(viewsets.ModelViewSet):
	queryset = Notification.objects.all()
	serializer_class = NotificationSerializer