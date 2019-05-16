from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Notification
		fields = ('title', 'body', 'created_at',)

