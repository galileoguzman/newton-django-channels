from django.db import models

# Create your models here.
class Notification(models.Model):
	title = models.CharField(max_length=120)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True) 
	upated_at = models.DateTimeField(auto_now =True)
	
	class Meta:
		ordering = ['-created_at']
	
	def __str__(self):
		return self.title