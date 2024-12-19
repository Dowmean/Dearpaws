from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    passed_away_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='pet_images/')  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
