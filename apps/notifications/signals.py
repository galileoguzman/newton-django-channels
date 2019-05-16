from django.db.models.signals import post_save 
from django.dispatch import receiver 
from asgiref.sync import async_to_sync 
from channels.layers import get_channel_layer 

from .models import Notification 

@receiver(post_save, sender=Notification) 
def notify_notification_save(sender, **kwargs):
	if "instance" in kwargs: 
		instance = kwargs["instance"] 
		# check if it is a new notification
		channel_layer = get_channel_layer() 
		async_to_sync(channel_layer.group_send)( 
			"notifications", {
				"type": "new.notification", 
				"event": "New Notification",
				"notification": {
					"title": instance.title,
					"body": instance.body
				}
			}
		)
