from django.db import models

# Create your models here.
class card(models.Model):
    nom=models.CharField(max_length=50)
    image=models.ImageField(upload_to="static/image")
    def __str__(self):
        return self.nom
