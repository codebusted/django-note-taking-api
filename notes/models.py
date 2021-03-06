from django.db import models

# Create your models here.
class Notes(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField(blank=True, null=False)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural ='Notes'
		ordering = ('title',)