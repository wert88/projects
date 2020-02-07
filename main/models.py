from django.db import models

class Movie(models.Model):
	title = models.CharField(max_length=200)
	file = models.FileField()
	
	def __str__(self):
		return self.title 
		
class Actor(models.Model):
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name
		
class ip(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
    	return self.ip_address + ' , ' + str(self.pub_date)