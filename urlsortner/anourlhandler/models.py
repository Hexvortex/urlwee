from django.db import models

# Create your models here.
class anoshort(models.Model):
    original_url = models.URLField(blank=False)
    short_query = models.CharField(blank=False,max_length=8)

    def __str__(self):
        return str(self.original_url)
    
